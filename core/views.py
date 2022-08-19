from fileinput import filename
import os 

from tracemalloc import get_object_traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse,HttpResponse, FileResponse

import django_boilerplate
import json

from . import models
from . import serializers
from django_boilerplate import settings

class BarDetail(APIView):
	def get(self, request, id,format=None):
		cocktailbar = get_object_or_404(models.Cocktailbar, pk=id)
		serializer = serializers.BarSerializer(cocktailbar)

		#cocktailbar = get_object_or_404(models.Cocktailbar, pk=id)
		# id = cocktailbar.cocktailbar_id
		# pngname = cocktailbar.cocktailbar_name
		# response = FileResponse(open(settings.BASE_DIR+'/static/cocktailbar/'+pngname+'.png', 'rb'))
		# response = cocktailbar.cocktailbar_img

		serializer = serializers.BarSerializer(cocktailbar)
		return Response(serializer.data)
	
	#수정중
class BarDetailImg(APIView):
	def get(self, request,id ,format=None):
		cocktailbar = get_object_or_404(models.Cocktailbar, pk=id)
		id = cocktailbar.cocktailbar_id
		pngname = cocktailbar.cocktailbar_name
		#response = FileResponse(open(settings.BASE_DIR+'/static/cocktailbar/'+pngname+'.png', 'rb'))
		response = FileResponse(open(settings.BASE_DIR+'/static/cocktailbar/'+pngname+'.png', 'rb'))

		return response
		
#http://127.0.0.1:8000/cocktailbar/test/1
class BarList(APIView):
	def get(self, request, format = None):
		cocktailbars = models.Cocktailbar.objects.all()
		serializer = serializers.BarSerializer(cocktailbars, many=True)
		return Response(serializer.data)

class CocktionaryDetail(APIView):
	def get(self, request, id,format=None):
		cocktionary = get_object_or_404(models.Cocktionary, pk=id)
		serializer = serializers.CocktionarySerializer(cocktionary)
		return Response(serializer.data)

class CocktionaryList(APIView):
	def get(self, request, format = None):
		cocktionarys = models.Cocktionary.objects.all()
		serializer = serializers.CocktionarySerializer(cocktionarys, many=True)
		return Response(serializer.data)







# class OrderTest(APIView):
# 	def get(self, request):
# 		orders = models.Order.objects.all()
# 		order_list = serializers.serialize('json', orders)
# 		return HttpResponse(order_list, content_type = "text/json-comment-filtered")
		



# class CocktionaryDetailViewTest(APIView):
# 	def get (self, request):
# 		cock = models.Cocktionary.objects.values()
# 		return JsonResponse({"data":cock}, status=200)
	
# 	def post(self,request):
# 		cock = json.loads(request.body)

# 		cocktionary_id = cock['cocktionary_id']
# 		cocktionary_cocktail_korname = cock['cocktionary_cocktail_korname']
# 		cocktionary_cocktail_engname = cock['cocktionary_cocktail_engname']
# 		cocktionary_cocktail_img = cock['cocktionary_cocktail_img']
# 		cocktionary_cocktail_ingredients = cock['cocktionary_cocktail_ingredients']
# 		cocktionary_cocktail_hashtag = cock['cocktionary_cocktail_hashtag']
# 		cocktionary_cocktail_recipe = cock['cocktionary_cocktail_recipe']

# 		models.Cocktionary(
# 			cocktionary_id = cocktionary_id,
# 			cocktionary_cocktail_korname=cocktionary_cocktail_korname,
# 			cocktionary_cocktail_engname=cocktionary_cocktail_engname,
# 			cocktionary_cocktail_img = cocktionary_cocktail_img,
# 			cocktionary_cocktail_ingredients=cocktionary_cocktail_ingredients,
# 			cocktionary_cocktail_hashtag = cocktionary_cocktail_hashtag,
# 			cocktionary_cocktail_recipe = cocktionary_cocktail_recipe
# 		).save()

# 		return HttpResponse(status = 200)
		

		