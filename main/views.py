from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, CreateView
from .forms import ContactModelForm

class HomeView(TemplateView):
    template_name = 'index.html'


class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')
