from django.shortcuts import render
from .forms import MessageForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Work
# Create your views here.
class CreateMessage(CreateView):
    model = Work
    template_name = 'work/contact_form.html'
    form_class = MessageForm
    success_url = reverse_lazy('thank_you')

