from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# test api function which return hello world
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")
