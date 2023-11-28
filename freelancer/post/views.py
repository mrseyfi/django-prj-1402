from datetime import datetime
from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from .forms import PostForm


def post_page(request, post_id):
    data_l = Post.objects.filter(id__lt=post_id).last()
    if not data_l:
        data_l = Post.objects.filter(id__lte=post_id).last()

    data_g = Post.objects.filter(id__gt=post_id).first()
    if not data_g:
        data_g = Post.objects.filter(id__gte=post_id).first()

    data = Post.objects.get(id=post_id)
    return render(request, 'post/post.html', {'post': data, 'post_l': data_l, 'post_g': data_g})


def delete(request, post_id):
    data = Post.objects.get(id=post_id).delete()
    messages.success(request, 'Post '+str(post_id)+' deleted successfully', 'success')
    return redirect('blog')


def edit(request, post_id):
    data = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            # cd = form.cleaned_data
            # (Post.objects.filter(id=post_id).update
            #                     (title=cd['title'],
            #                      body=cd['body'],
            #                      ))
            messages.success(request, 'Thank you! Your post has been successfully saved.')
            return redirect('blog')
    else:
        form = PostForm(instance=data)
    return render(request, 'post/edit.html', {'form': form})


def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            # cd = form.cleaned_data
            # (Post.objects.create(title=cd['title'],
            #                      body=cd['body']
            #                      ))
            messages.success(request, 'Thank you! Your post has been successfully saved.')
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'post/edit.html', {'form': form})


def blog_page(request):
    data = Post.objects.all()
    user = 'admin'
    return render(request, 'post/blog.html', {'posts': data,'user': user})
