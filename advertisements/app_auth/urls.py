from django.urls import path
from .views import login_view, register_view, profile_view, SignUp

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('register/', SignUp.as_view(), name='register')
]
