from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Work(models.Model):
    my_validator = RegexValidator(r"(^[\d]{3}) ([\d]{7}$)",'formato numero telefono "xxx xxxxxxx"')
    #visible fields
    name = models.CharField(_('name'),max_length=250)
    email = models.EmailField(_('email'))
    phone = models.CharField(_('phone'),max_length=20,validators=[my_validator])
    message = models.TextField(_('message'))
    #fields for the admin
    created = models.DateTimeField(_('created'),auto_now_add=True)
    modified = models.DateTimeField(_('modified'),auto_now=True)
    read = models.BooleanField(_('read'),default=False)
    accepted  =models.BooleanField(_('accepted'),default=False)
    working = models.BooleanField(_('working'),default=False)
    finished  = models.BooleanField(_('finished'),default=False)
    class Meta:
        verbose_name_plural = 'Mesaje'
        verbose_name = 'Mesaj'


