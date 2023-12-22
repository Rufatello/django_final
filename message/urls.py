from django.urls import path
from . import views
from message.apps import MessageConfig

app_name = MessageConfig.name
urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    ]