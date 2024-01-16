from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import math
# Create your views here.

# test api function which return hello world
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

# scientific calculator api function
def square_root(request):
    if request.method == "GET":
        data=request.GET
        try:
            num1 = float(data.get("num1"))
            result = math.sqrt(num1)
            return JsonResponse({"Square Root is ": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})

def power(request):
    if request.method == "GET":
        data=request.GET
        try:
            num1 = float(data.get("num1"))
            num2 = float(data.get("num2"))
            result = math.pow(num1,num2)
            return JsonResponse({"Power num1 to num2 is ": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})

def log(request):
    if request.method == "GET":
        data=request.GET
        try:
            num1 = float(data.get("num1"))
            result = math.log(num1)
            return JsonResponse({"Log of num1 is ": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})

def log10(request):
    if request.method == "GET":
        data=request.GET
        try:
            num1 = float(data.get("num1"))
            result = math.log10(num1)
            return JsonResponse({"Log10 of num1 is ": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})
    
def sin(request):
    if request.method == "GET":
        data=request.GET
        try:
            num1 = float(data.get("num1"))
            result = math.sin(num1)
            return JsonResponse({"Sin of num1 is ": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})

def cos(request):
    if request.method == "GET":
        data=request.GET
        try:
            num1 = float(data.get("num1"))
            result = math.cos(num1)
            return JsonResponse({"Cos of num1 is ": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})

def tan(request):
    if request.method == "GET":
        data=request.GET
        try:
            num1 = float(data.get("num1"))
            result = math.tan(num1)
            return JsonResponse({"Tan of num1 is ": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})

def factorial(request):
    if request.method == "GET":
        data=request.GET
        try:
            num1 = int(data.get("num1"))
            result = math.factorial(num1)
            return JsonResponse({"Factorial of num1 is ": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})

def exponential(request):
    if request.method == "GET":
        data=request.GET
        try:
            num1 = float(data.get("num1"))
            result = math.exp(num1)
            return JsonResponse({"Exponential of num1 is ": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})