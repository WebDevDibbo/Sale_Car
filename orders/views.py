from django.shortcuts import render,redirect
from django.contrib import messages
from orders.models import OrderModel
from cars.models import PostCar
from orders.forms import OrderForm
from . import models
# Create your views here.
def Orders(request,id):

    car_item = PostCar.objects.get(pk=id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if car_item.quantity >= quantity:
                car_item.quantity -= quantity
                car_item.save()

                order_history = OrderModel.objects.create(
                    car = car_item,
                    user = request.user,
                    quantity = quantity,
                    totalPrice = car_item.price * quantity,
                )
                messages.success(request,"Ordered Successful")
                return redirect('detail_post', id = car_item.pk)
            else:
                messages.error(request, 'Insufficient')
        
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form':form})