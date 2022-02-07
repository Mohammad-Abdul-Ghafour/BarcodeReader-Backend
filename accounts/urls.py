from django.contrib import admin
from django.urls import path 
from .views import CustomUserCreateView , CustomUserDetailView

urlpatterns = [
    path('', CustomUserCreateView.as_view()),
    path('<int:pk>', CustomUserDetailView.as_view()),
]