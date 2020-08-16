from django.shortcuts import render
from django.views.generic.list import ListView

from . models import Project

class HomeView(ListView):
    model = Project
    template_name = 'portfolio/home.html'
