from .models import BlogIndexPage,BlogPage,BlogTagIndexPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from taggit.models import Tag

@register(BlogIndexPage)
class BlogIndexPage(TranslationOptions):
    fields =(
        'intro',
    )
@register(BlogPage)
class BlogPAgeTR(TranslationOptions):
    fields = (
        'description',
        'body',

    )
@register(Tag)
class TagTR(TranslationOptions):
    fields = (
        'name',
    )
@register(BlogTagIndexPage)
class BlogTagIndexPageTR(TranslationOptions):
    pass