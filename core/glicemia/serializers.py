from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Glicemia

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class GlicemiaSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')

    class Meta:
        model = Glicemia
        fields = ['id', 'time', 'value', 'title', 'description', 'created_at', 'user_id']

    def create(self, validated_data):
        user = validated_data.pop('user')  # Get the 'user' instance from validated_data
        glicemia = Glicemia.objects.create(user=user, **validated_data)
        return glicemia