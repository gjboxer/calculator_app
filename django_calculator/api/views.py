from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import math

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def addition(request):
    if request.method == "GET":
        data = request.GET
        try:
            num1 = float(data.get("num1"))
            num2 = float(data.get("num2"))

            result = num1 + num2
            return JsonResponse({"Addition of num1 by num2 is ": result})
    
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})
    
def subtract(request):
    if request.method == "GET":
        data = request.GET
        try:
            num1 = float(data.get("num1"))
            num2 = float(data.get("num2"))
            
            result = num1 - num2
            return JsonResponse({"Subtraction of num1 by num2 is ": result})
            
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})
    
def multiply(request):
    if request.method == "GET":
        data = request.GET
        try:
            num1 = float(data.get("num1"))
            num2 = float(data.get("num2"))

            result = num1 * num2
            return JsonResponse({"Multiplication of num1 by num2 is ": result})

        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})
    
def divide(request):
    if request.method == "GET":
        data = request.GET
        try:
            num1 = float(data.get("num1"))
            num2 = float(data.get("num2"))

            if num2 != 0:
                result = num1 / num2
                return JsonResponse({"Division of num1 by num2 is ": result})
            else:
                return JsonResponse({"error": "Cannot divide by zero"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "GET request required."})