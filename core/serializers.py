from csv import excel
from unicodedata import name
from rest_framework import serializers
from .models import Cocktailbar, Cocktionary
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
        #이미지 테스트 해보려고 img 일단 serializer에서 배제함.
        #exclude = ['cocktailbar_img']
        fields = '__all__'
        

class CocktionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktionary
        fields = '__all__'