from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, View, UpdateView, ListView, DeleteView

from message.models import Client


class HomeTemplateView(TemplateView):
    template_name = 'message/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class ContactView(View):
    template_name = 'message/kontact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(name, phone, message)
        return render(request, self.template_name)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'message/client_create.html'
    success_url = reverse_lazy('message:client_list')
    fields = ('first_name', 'last_name', 'surname', 'email',)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'message/update_client.html'
    success_url = reverse_lazy('message:client_list')
    fields = ('first_name', 'last_name', 'surname', 'email',)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого клиента")
        return self.object


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'message/client_list.html'



class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'message/delete_client.html'
    success_url = reverse_lazy('message:client_list')
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого клиента")
        return self.object