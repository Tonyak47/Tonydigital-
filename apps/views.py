from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogPostSerializer
from .models import blog_post

# Create your views here.
def index(request):
    return render(request, 'index.html')

def error(request):
    return render(request, '404.html')

def education(request):
    return render(request, 'education.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    if request.method == "POST":
        NAME= request.POST.get('name')
        num = request.POST.get('num')
        email = request.POST.get('email')
        message= request.POST.get('message')
        log= blog_post( name = NAME, email = email, message = message, num = num)
        log.save()
        return redirect('index')
    return render(request, 'contact.html')

def blog(request):
    messages= blog_post.objects.all()
    return render(request, 'blog.html', {'messages': messages})

def about(request):
    return render(request, 'about.html')

class BlogPostListCreateAPIView(APIView):
    def get(self, request):
        posts = blog_post.objects.all()
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BlogPostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
