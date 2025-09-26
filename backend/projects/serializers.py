from rest_framework import serializers
from .models import Project, Technology, Role
from users.serializers import UserSerializer

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):
    technologies = serializers.StringRelatedField(many=True)
    roles = serializers.StringRelatedField(many=True)
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'college_name', 'posted_by', 'technologies', 'roles', 'github_url', 'created_at']
