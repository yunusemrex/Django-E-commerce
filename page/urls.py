from django.urls import path
from .views import carousel_create, carousel_list, carousel_update, index



urlpatterns = [
    path('', index, name='index'),
    path('carousel_list/', carousel_list, name='carousel_list'), 
    path('carousel_create/', carousel_create, name='carousel_create'),
] 