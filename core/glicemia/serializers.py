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
    class Meta:
        model = Glicemia
        fields = ['id', 'time', 'value', 'title', 'description', 'created_at']
        read_only_fields = ['created_at']  # Mark 'created_at' field as read-only

    def create(self, validated_data):
        # Get the authenticated user from the request context
        user = self.context['request'].user

        # Create the 'Glicemia' instance with the authenticated user
        glicemia = Glicemia.objects.create(user=user, **validated_data)
        return glicemia