from django.urls import path
from rest_framework import routers
from .views import *

app_name = 'ticket_api'

# Register router for model view sets
router = routers.SimpleRouter()
router.register('ticket', TicketViewSet)
router.register('message', MessageViewSet)

# define urlpatterns for none model view set APIViews
urlpatterns = [
    path('ticket-messages/<int:pk>/', TicketMessagesAPIView.as_view(), name='ticket messages'),
]

# Add router urls to urlpatterns
urlpatterns += router.urls
