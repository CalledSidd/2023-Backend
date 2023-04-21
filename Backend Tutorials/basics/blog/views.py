from django.shortcuts import render
from blog.models import Post
from django.urls import reverse

# Create your views here.
def home(request):
    posts = Post.objects.all().filter(status='published')
    context = {'post': posts}
    return render(request, 'home.html', context) 


def blog(request, id):
    blog = Post.objects.get(id = id)
    print(blog)
    context = {'blog' : blog}
    return render(request, 'post.html', context)


def about(request):
    name = "Sidharth S"
    url = "/"
    context = {
        'name': name,
        'url' : url
    }
    return render(request, 'about.html', context)