from django.urls import path
from .views import RegisterAPI


app_name = 'authentication'


urlpatterns = [
  path('register/', RegisterAPI.as_view(), name='register'),
]