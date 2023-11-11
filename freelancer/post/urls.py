from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.post_page),
    path('', views.blog_page),
    # Enter the app name in following syntax for this to work
]