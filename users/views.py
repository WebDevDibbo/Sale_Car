from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from orders.models import OrderModel


# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form =  forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    else:
        register_form =  forms.RegistrationForm()
    return render(request,'register.html',{'form':register_form, 'type' : 'Register'})


class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self,form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request, 'information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['order_history'] = OrderModel.objects.all()
        return context



@login_required
def editProfile(request):
    if request.method == 'POST':
        profile_form =  forms.ChangeUserData(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form =  forms.ChangeUserData(instance=request.user)
    return render(request,'update_profile.html',{'form':profile_form})    



class UserLogoutView(LogoutView):
    next_page = 'home'
