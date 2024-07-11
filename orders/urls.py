from django.urls import path
from . import views

urlpatterns = [
    path("order/<int:id>/", views.Orders, name="orders"),
]