from rest_framework import viewsets, mixins
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView
from .permissions import *


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsTicketOwnerOrReadOnly()]
        return [IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = TicketSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MessageCreateUpdateSerializer
        return MessageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsMessageOwnerOrReadOnly()]
        return [IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class TicketMessagesAPIView(ListAPIView):
    serializer_class = TicketMessagesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Message.objects.filter(ticket=self.kwargs.get('pk'))
