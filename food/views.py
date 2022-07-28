from django.shortcuts import render
from pkg_resources import set_extraction_path
from .models import Meal
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MealSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def meal_list(request):
    meals = Meal.objects.all()
    serializer = MealSerializer(meals, many= True)
    return Response(serializer.data)


@api_view(['POST'])
def meal_create(request):
    serializer = MealSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def meal_details(request, id):
    try:
        meal = Meal.objects.get(pk=id)
    except Meal.DoesNotExist:
        return Response(status= status.HTTP_404_NPT_FOUND)
    if request.method == 'GET':
        serializer = MealSerializer(meal)
        return Response(serializer.data)
        
    