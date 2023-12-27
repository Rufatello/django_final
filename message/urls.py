from django.urls import path
from . import views
from message.apps import MessageConfig

app_name = MessageConfig.name
urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('client_create/', views.ClientCreateView.as_view(), name='client_create'),
    path('update/<int:pk>', views.ClientUpdateView.as_view(), name='update_client'),
    path('list/', views.ClientListView.as_view(), name='client_list'),
    path('delete/<int:pk>/detail/', views.ClientDeleteView.as_view(), name='delete'),
    path('mailings_list/', views.MailingsListView.as_view(), name='mailings_list'),
    path('mailings_create/', views.MailingsCreateView.as_view(), name='mailings_create'),
    ]