from django import template
from django.utils import  translation
from django.utils.translation import gettext_lazy as _
from django.urls import resolve,reverse_lazy,translate_url
from django.utils.encoding import force_str
try:
    from wagtail.core.models import Page, Site,SiteRootPath
    from wagtail.core.templatetags.wagtailcore_tags import pageurl,slugurl
except ImportError:
    from wagtail.wagtailcore.models import Page
    from wagtail.wagtailcore.templatetags.wagtailcore_tags import pageurl

register=template.Library()

@register.simple_tag(takes_context=True)
def page_lang(context, lang=None, page=None, *args, **kwargs):
    current_language=translation.get_language()
    site = Site.find_for_request(context['request'])
    if 'request' in context and lang and current_language and page:
        path= context['request'].path

        root_slug = getattr(site.root_page,"slug_{}".format(lang),None)
        temp_path = getattr(page,"url_path_{}".format(lang),None)
        if temp_path:
            trans_path = temp_path.replace(root_slug+"/","/{}/".format(lang))
            return trans_path
    tmp1 = reverse_lazy(resolve(context['request'].path).url_name)

    return translate_url(force_str(tmp1),lang)

@register.simple_tag(takes_context=False)
def get_slug(page=None,*args,**kwargs):
    current_language = translation.get_language()
    if page:
        temp_slug = getattr(page, "slug_{}".format(current_language), None)
        if temp_slug:
            return temp_slug
    return None
@register.simple_tag(takes_context=True)
def tag_url(context):
    current_language=translation.get_language()
    return "/{}/tags/".format(current_language)
