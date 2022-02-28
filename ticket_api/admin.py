from django.contrib import admin
from .models import *


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('creator', 'status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'ticket',)
