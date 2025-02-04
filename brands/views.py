from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms


# Create your views here.
def AddBrand(request):
    if request.method == 'POST':
        brand_form = forms.BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('home')
    else:
        brand_form = forms.BrandForm()
    return render(request, 'add_brand.html', {'form' : brand_form})