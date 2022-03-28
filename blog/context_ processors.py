from wagtail.core.models import Site
def getHomepage(request):
    site = Site.find_for_request(request=request)
    return {"homepage":site.root_page}