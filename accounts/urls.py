from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = 'accounts'

router = routers.SimpleRouter()
router.register('profile', UserProfileInfoUpdateRetrieveViewSet)

urlpatterns = [
    path('teachers/login/', TeacherLoginWithPasswordAPIView.as_view(), name='teacher-login'),
]

urlpatterns += router.urls
