from unicodedata import decimal
from django.db import models

# Create your models here.
class Cocktailbar(models.Model):
    cocktailbar_id = models.CharField(max_length=15)
    cocktailbar_name = models.CharField(max_length=30)
    cocktailbar_img = models.ImageField(blank=True, null=True, upload_to='static/cocktailbar')
    client_password = models.CharField(max_length=15)
    cocktailbar_description = models.CharField(max_length=100)
    #그냥 "#라임 #얼음" 이런식으로 해서 예쁘게 문자열 전체 그대로 넣는 방식
    cocktailbar_hashtags = models.TextField()
    cocktailbar_stars = models.DecimalField(max_digits=2, decimal_places=1)
    cocktailbar_address = models.TextField()
    cocktailbar_worktime = models.TextField()

class Cocktionary(models.Model):
    cocktionary_id = models.IntegerField()
    cocktionary_cocktail_korname = models.CharField(max_length=100)
    cocktionary_cocktail_engname = models.CharField(max_length=100)
    cocktionary_cocktail_img = models.ImageField(blank=True, null=True, upload_to='static/cocktail')
    cocktionary_cocktail_ingredients = models.TextField()
    cocktionary_cocktail_hastag = models.TextField()
    cocktionary_cocktail_recipe = models.TextField()

class Signature(models.Model):
    cocktailbar_id = models.CharField(max_length=15)
    sig_cocktail_img = models.ImageField(blank=True, null=True, upload_to='static/signature')
    sig_cocktail_korname = models.CharField(max_length=30)

# class Order(models.Model):
#     order_num = models.IntegerField()
#     order_time = models.DateField()
#     client_id = models.CharField(max_length=15)
#     client_cocktail = models.CharField(max_length=30)
#     #일단은 char로 해두고 serializer로 여러개 가능한지 체크하기
#     #일단 얘를 가져오고 얘를 serialize 해야할 것 같음..
#     client_detail_customizing = models.CharField(max_length=30)
#     order_check = models.BooleanField()
