from django.shortcuts import render

from django.views.generic import TemplateView, DetailView
from app.models import SherlockBook
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class SherlockBookDetailView(DetailView):
    model = SherlockBook
