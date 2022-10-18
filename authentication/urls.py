from django.urls import path
from .apis import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views


app_name = 'authentication'


urlpatterns = [
  path('user/', UserAPI.as_view(), name='user details'),
  path('register/', RegisterAPI.as_view(), name='register'),
  path('login/', LoginAPI.as_view(), name='login'),
  path('logout/', knox_views.LogoutView.as_view(), name='logout'),  # type: ignore
  path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]