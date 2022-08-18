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

