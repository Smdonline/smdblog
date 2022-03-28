from django.db import models
from wagtail.core.models import Page

# Create your models here.
class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(public=True).order_by('-created')



class Comment(models.Model):
    page = models.ForeignKey(Page,related_name="page_comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=80,blank=None)
    email = models.EmailField(blank=None)
    text = models.TextField(blank=None)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    objects = models.Manager()
    public_comments= CommentManager()



