from django.shortcuts import render
from .models import Post


def post_page(request,post_id):
    data_l = Post.objects.filter(id__lt=post_id).last()
    if not data_l:
        data_l = Post.objects.filter(id__lte=post_id).last()

    data_g = Post.objects.filter(id__gt=post_id).first()
    if not data_g:
        data_g = Post.objects.filter(id__gte=post_id).first()

    data = Post.objects.get(id=post_id)
    return render(request, 'post/post.html', {'post': data, 'post_l': data_l, 'post_g': data_g})


def blog_page(request):
    data = Post.objects.all()
    user = 'admin'
    return render(request, 'post/blog.html', {'posts': data,'user': user})
