from django.urls import path
from .api import RegisterAPI, LoginAPI
from knox import views as knox_views


app_name = 'authentication'


urlpatterns = [
  path('register/', RegisterAPI.as_view(), name='register'),
  path('login/', LoginAPI.as_view(), name='login'),
  path('logout/', knox_views.LogoutView.as_view(), name='logout'),  # type: ignore
  path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]