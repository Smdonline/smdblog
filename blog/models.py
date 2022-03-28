from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.models import Page,Orderable

from wagtail.core.fields import RichTextField,StreamField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase,TagBase
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
"""
Pgae containing all the blogs paginated by 5 
"""
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro',classname="full")
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request,*args,**kwargs)
        all_posts=self.get_children().live().order_by('-first_published_at').exclude(slug="about")
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)


        context["posts"] = posts
        return context
"""
    
"""
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
"""

"""
class BlogPage(Page):

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="Add Image+"
    )
    description = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(cassname="img-fluid")),
    ])
    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('description'),
        FieldPanel('tags'),
        StreamFieldPanel('body')
    ]
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    parent_page_types = ['blog.BlogIndexPage','home.HomePage']
    subpage_types = []
    """
    return page with all comments paginated by 5
    """
    #TODO create ajax request to browse comments
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request,*args,**kwargs)

        post_comments=self.page_comments.all().filter(public=True).order_by('-created')
        paginator = Paginator(post_comments,5)
        page = request.GET.get('page')
        try:

            comments = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            comments = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            comments = paginator.page(paginator.num_pages)
        context['comments'] = comments
        return context
    def get_short_description(self):
        if len(self.description)>5:
            temp=self.description[0:50]
            print(temp)
            return temp
        return self.description
"""
    list all the pages containig one tag
    return none if any
"""
class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context