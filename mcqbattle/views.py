from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, World. You are at prashik's homepage")
    