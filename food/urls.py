from django.urls import path
from food import views

urlpatterns = [
    path('meals',views.meal_list, name='meals'),
    path('meals/create',views.meal_create, name='create meals'), 
    path('meals/details/<int:id>/',views.meal_details, name='meal details'), 
]
