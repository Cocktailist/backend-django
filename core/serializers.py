from unicodedata import name
from rest_framework import serializers
from .models import Cocktailbar
# class Cocktailbar_Serializer(serializers.Serializer):
#     cocktailbar_id = serializers.CharField()
#     cocktailbar_name = serializers.CharField()
#     cocktailbar_img = serializers.ImageField()
#     client_password = serializers.CharField()
#     cocktailbar_description = serializers.CharField()
#     cocktailbar_hashtags = serializers.TextField()


class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktailbar
        fields = '__all__'