from rest_framework import serializers
from accounts.models import  User


class ObtainTokenSerializer(serializers.Serializer):
    teacher_id = serializers.CharField()
    token = serializers.CharField(max_length=128, allow_null=False)
    refresh = serializers.CharField(max_length=128, allow_null=False)


class TeacherLoginWithPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=68, min_length=3, required=True)
    password = serializers.CharField(min_length=6, required=True)


class UserProfileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'username', 'email')
