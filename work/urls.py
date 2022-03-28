from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns =[
    path('',views.CreateMessage.as_view(),name='new_message'),
    path('thank_you/',TemplateView.as_view(template_name='work/thank_you.html'),name='thank_you'),


]