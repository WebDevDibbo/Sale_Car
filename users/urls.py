from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('profile/', views.Profile.as_view(), name = 'profile'),
    path('profile/edit/', views.editProfile, name = 'edit_profile'),
]