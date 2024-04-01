from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class BasePageView(TemplateView):
    template_name = 'base.html'


class MainPageView(TemplateView):
    template_name = 'main.html'


class SalomPageView(TemplateView):
    template_name = 'salom.html'
