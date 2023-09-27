from django.shortcuts import render

from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = '../templates/base.html'
