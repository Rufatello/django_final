from django.shortcuts import render
from django.views.generic import CreateView, TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'message/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context