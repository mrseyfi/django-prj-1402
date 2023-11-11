from django.shortcuts import render
from .models import Post


def post_page(request):
    data = Post.objects.first()
    return render(request, 'post/post.html', {'posts': data})


def blog_page(request):
    data = Post.objects.all()
    return render(request, 'post/blog.html', {'posts': data})
