from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='home'),
    path('contact/', views.contact_page),
    path('about/', views.about_page),
    path('portfolio/', views.portfolio_page),
    # Enter the app name in following syntax for this to work
]