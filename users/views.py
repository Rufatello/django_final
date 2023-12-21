import random
from django.conf import settings
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View, UpdateView, TemplateView
from users.models import User
from users.forms import UserForm, UserFormUpdate, PasswordChangingForm


class UserTemplateView(TemplateView):
    template_name = 'users/templates.html'
def LogoutUser(request):
    logout(request)

    return redirect('message:home')

class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class RegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserForm
    success_url = reverse_lazy('users:code')
    def form_valid(self, form):
        new_pass = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        new_user = form.save(commit=False)
        new_user.code = new_pass
        new_user.save()
        send_mail(
            subject='Подтверждение регистрации',
            message=f' Введите код: {new_user.code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        return super().form_valid(form)




class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangingForm
  success_url = reverse_lazy('users:login')
  template_name = 'users/user_password.html'



class CodeView(View):
    model = User
    template_name = 'users/code.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        code = request.POST.get('code')
        user = User.objects.filter(code=code).first()

        if user is not None and user.code == code:
            user.is_active = True
            user.save()
            return redirect('users:login')

class UserUpdate(UpdateView):
    model = User
    template_name = 'users/update_profile.html'
    form_class = UserFormUpdate
    success_url = reverse_lazy('message:home')

    def get_object(self, queryset=None):
        return self.request.user

def new_password(request):
    new_pass = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    send_mail(
        subject='Новый пароль',
        message=f'Новый пароль {new_pass}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_pass)

    request.user.save()

    return redirect(reverse('users:login'))
