from django.shortcuts import render

def index(request):
   return render(request, 'main/index.html')

def material(request):
   return render(request, 'main/material.html')

def others(request):
   return render(request, 'main/others.html')

