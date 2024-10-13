# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World! , I'm Home Page.")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("Hello World! , I'm About Page.")
    return render(request, 'about.html')