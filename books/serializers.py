from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class MembersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'