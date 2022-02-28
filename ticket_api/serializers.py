from rest_framework import serializers
from .models import *


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('subject',)


class MessageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'ticket', 'image',)


class MessageSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(read_only=True, many=False)

    class Meta:
        model = Message
        fields = '__all__'


class TicketMessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
