from rest_framework.serializers import ModelSerializer
from .models import User

class User_serializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_type',
            'user_id',
            'name',
            'email',
            'join_date_time',
            'google_login',
        ]
