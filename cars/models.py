from django.db import models
from brands.models import Brand

# Create your models here.

class PostCar(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='cars/media/uploads', blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(PostCar, on_delete=models.CASCADE, related_name='comments', default=None)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comments by {self.name}'
