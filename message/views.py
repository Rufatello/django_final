from django.shortcuts import render
from django.views.generic import CreateView, TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'message/index.html'
