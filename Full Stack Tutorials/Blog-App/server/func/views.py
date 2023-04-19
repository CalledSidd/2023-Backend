from django.shortcuts import render

from func.models import  BlogPost

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

# Create your views here.
class CreateBlogPost(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer