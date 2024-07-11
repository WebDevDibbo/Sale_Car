from django.contrib.auth.models import User
from django.db import models
from cars.models import PostCar


# Create your models here.
class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(PostCar, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    totalPrice = models.IntegerField()