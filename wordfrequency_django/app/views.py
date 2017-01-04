from django.shortcuts import render

from django.views.generic import DetailView, ListView
from app.models import SherlockBook
# Create your views here.


class IndexView(ListView):
    model = SherlockBook


class SherlockBookDetailView(DetailView):
    model = SherlockBook
