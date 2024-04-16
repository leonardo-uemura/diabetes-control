from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import Glicemia
from .serializers import GroupSerializer, UserSerializer, GlicemiaSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class GlicemiaViewSet(viewsets.ModelViewSet):
    queryset = Glicemia.objects.all().order_by('time')
    serializer_class = GlicemiaSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authenticated user

    def get_serializer_context(self):
        # Pass request object to serializer context
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    # Optional: Customize queryset based on user (e.g., show only user's data)
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)