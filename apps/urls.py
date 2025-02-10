from django.urls import path
from .views import BlogPostListCreateAPIView
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('education/', views.education, name= 'education'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('404/', views.error, name='404'),
    path('contact/blog/', views.blog, name='blog'),
    path('api/blog-posts/', BlogPostListCreateAPIView.as_view(), name='blog-post-list-create')
]
