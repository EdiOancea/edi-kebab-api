from rest_framework import serializers

from app.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'level',
            'is_active',
        ]
        read_only_fields = ['is_active', 'id']
