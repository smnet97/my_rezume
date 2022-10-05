from django.shortcuts import render
from .models import WorkModel
from django.views.generic import ListView, DetailView


class WorkListView(ListView):
    model = WorkModel
    template_name = 'works.html'


class WorkDetailView(DetailView):
    model = WorkModel
    template_name = 'z_dashbord_ichi_workss.html'
