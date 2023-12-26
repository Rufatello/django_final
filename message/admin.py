from django.contrib import admin
from message.models import Message, Mailings, Client


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'body', 'name',)

@admin.register(Mailings)
class MailingsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'state',)
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name',)