from .serializers import *
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from django.utils import timezone
from django.contrib import auth
from rest_framework import viewsets, mixins
from .permissions import IsProfileOwner
from rest_framework.permissions import IsAuthenticated


class TeacherLoginWithPasswordAPIView(generics.GenericAPIView):
    serializer_class = TeacherLoginWithPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            teacher = auth.authenticate(username=serializer.data.get('username'),
                                        password=serializer.data.get('password'))
            if teacher:
                refresh_token = RefreshToken.for_user(teacher)
                return Response(status=status.HTTP_200_OK, data=ObtainTokenSerializer({
                    'teacher_id': teacher.id,
                    'refresh': str(refresh_token),
                    'token': str(refresh_token.access_token),
                }).data)
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={'error: Authentication failed. Invalid username or password'}
            )
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class UserProfileInfoUpdateRetrieveViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileInfoSerializer
    permission_classes = (IsAuthenticated, IsProfileOwner)
