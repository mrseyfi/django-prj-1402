from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_page, name="blog"),
    path('<int:post_id>/', views.post_page, name="post"),
    path('delete/<int:post_id>/', views.delete, name="deletePost"),
    path('edit/<int:post_id>/', views.edit, name="editPost"),
    path('new/', views.new, name="newPost"),
    # Enter the app name in following syntax for this to work
]