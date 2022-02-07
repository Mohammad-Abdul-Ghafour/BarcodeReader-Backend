import imp
from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cosmetics
from .serializer import CosmaticsSerializer

class CosmeticsCreateView(ListCreateAPIView):
    queryset = Cosmetics.objects.all()
    serializer_class = CosmaticsSerializer

class CosmeticsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cosmetics.objects.all()
    serializer_class = CosmaticsSerializer