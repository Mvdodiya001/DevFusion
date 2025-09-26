from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow anyone to view, but only authenticated users to create

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
