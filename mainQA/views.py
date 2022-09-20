from django.http import JsonResponse
from .models import Event, Question
from .serializers import EventSerializer, QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def events_list(request):

  if request.method == 'GET':
    allEvents = Event.objects.all()
    serializer = EventSerializer(allEvents, many=True)
    return JsonResponse({'events': serializer.data})

  elif request.method == 'POST':
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


def questions_list(request):
  allQuestions = Question.objects.all()
  serializer = QuestionSerializer(allQuestions, many=True)
  
  return JsonResponse({'questions': serializer.data})