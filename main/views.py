from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, CreateView
from .forms import ContactModelForm
from blogs.models import BlogModel
from works.models import WorkModel


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs2'] = BlogModel.objects.all()[:2]
        context['works3'] = WorkModel.objects.all().order_by('-id')[:3]
        return context


class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')
