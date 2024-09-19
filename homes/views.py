from django.shortcuts import render

def home(request):
    return render(request, 'homes/home.html')

def about(request):
    return render(request, 'homes/about.html')