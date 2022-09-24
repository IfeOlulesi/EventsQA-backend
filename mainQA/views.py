from django.http import JsonResponse
from .models import Event, Question
from .serializers import EventSerializer, QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET', 'POST'])
def events_list(request):

  if request.method == 'GET':
    allEvents = Event.objects.all()
    serializer = EventSerializer(allEvents, many=True)
    return JsonResponse({'events': serializer.data})


  if request.method == 'POST':
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


# @csrf_exempt
@api_view(['GET', 'POST'])
def questions_list(request):
  if request.method == 'GET':
    allQuestions = Question.objects.all()
    serializer = QuestionSerializer(allQuestions, many=True)
    return JsonResponse({'questions': serializer.data})


  if request.method == 'POST':
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)