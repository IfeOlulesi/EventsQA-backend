from django.urls import path
from . import views

app_name = 'api/v1'


urlpatterns = [
  path('events/', views.events_list),

  path('questions/', views.questions_list),
]