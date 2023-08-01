from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_list),
    path('<pk>/', views.car_detail),
    path('<str:make>', views.cars_by_make),
    
]