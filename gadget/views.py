from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
    )
from .models import Gadget
# Create your views here.

class AllGadtgetsView(ListView):
    model = Gadget
    template_name = 'index.html'

class GadgetDetailView(DetailView):
    model = Gadget
