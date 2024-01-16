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
    
def subtract(request):
    if request.method == "GET":
        data = request.GET
        try:
            num1 = float(data.get("num1"))
            num2 = float(data.get("num2"))
            
            result = num1 - num2
            return JsonResponse({"Subtraction of num1 by num2 is ": result})
            

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
    
def multiply(request):
    if request.method == "GET":
        data = request.GET
        try:
            num1 = float(data.get("num1"))
            num2 = float(data.get("num2"))

            result = num1 * num2
            return JsonResponse({"Multiplication of num1 by num2 is ": result})

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