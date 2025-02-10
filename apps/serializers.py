from rest_framework import serializers
from .models import blog_post

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_post
        fields = '__all__'