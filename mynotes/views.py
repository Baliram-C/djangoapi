from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import serializers
from .models import Mynotes
from .serializers import CourseSerializer
# Create your views here.
class Mynoteview(viewsets.ModelViewSet):
	queryset = Mynotes.objects.all()
	serializer_class = CourseSerializer