from django.urls import path
from . import apis
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api/v1'


urlpatterns = [
  path('events/', apis.events_list),

  path('events/<int:id>', apis.events_detail),

  path('questions/', apis.questions_list),

  path('questions/<int:id>', apis.questions_detail),

  path('getQuestionsByEventId/', apis.questions_by_eventId),
]


urlpatterns = format_suffix_patterns(urlpatterns)