from django.urls import path
from . import views


urlpatterns = [
    path('<int:post_id>/', views.post_page, name="post"),
    path('', views.blog_page),
    # Enter the app name in following syntax for this to work
]