from django.shortcuts import render
from cars.models import PostCar
from brands.models import Brand
def home(request, brand_slug = None):
    data = PostCar.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = PostCar.objects.filter(brand = brand)
    brands = Brand.objects.all()
    return render(request, 'home.html', {'data':data, 'brand' : brands})

    