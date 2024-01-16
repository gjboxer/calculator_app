from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("square_root/", views.square_root, name="square_root"),
    path("power/", views.power, name="power"),
    path("log/", views.log, name="log"),
    path("log10/", views.log10, name="log10"),
    path("sin/", views.sin, name="sin"),
    path("cos/", views.cos, name="cos"),
    path("tan/", views.tan, name="tan"),
    path("factorial/", views.factorial, name="factorial"),
    path("exponential/", views.exponential, name="exponential"),
]
