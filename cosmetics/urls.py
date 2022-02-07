from django.contrib import admin
from django.urls import path 
from .views import CosmeticsCreateView , CosmeticsDetailView

urlpatterns = [
    path('', CosmeticsCreateView.as_view()),
    path('<int:pk>', CosmeticsDetailView.as_view()),
]