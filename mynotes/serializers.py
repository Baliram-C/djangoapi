from rest_framework import serializers
from .models import Mynotes

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Mynotes
		fields = ('id','url','name','language','price')