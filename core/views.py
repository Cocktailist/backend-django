from tracemalloc import get_object_traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import render, HttpResponse, redirect

from . import models
from . import serializers

class BarDetail(APIView):
	def get(self, request, id,format=None):
		cocktailbar = get_object_or_404(models.Cocktailbar, pk=id)
		serializer = serializers.BarSerializer(cocktailbar)
		return Response(serializer.data)

class BarList(APIView):
	def get(self, request, format = None):
		cocktailbars = models.Cocktailbar.objects.all()
		serializer = serializers.BarSerializer(cocktailbars, many=True)
		return Response(serializer.data)

# def index(request):
# 	return render(request, 'core/index.html')

def index(request):
    return HttpResponse("http response 테스트")