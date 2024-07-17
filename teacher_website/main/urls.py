
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('material', views.material, name='material'),
    path('others', views.others, name='others'),
    
]