from django.core.exceptions import ObjectDoesNotExist
from .models import Event, Question
from .serializers import EventSerializer, QuestionSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class WriteOnly(BasePermission):
  def has_permission(self, request, view):
    if request.method == "POST":
      return True
    else:
      return False


#Read all Events  | Create Single Event
@api_view(['GET', 'POST'])
def events_list(request, format=None):

  if request.method == 'GET':
    allEvents = Event.objects.all()
    serializer = EventSerializer(allEvents, many=True)
    return Response(serializer.data)


  if request.method == 'POST':
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#Read single event | Update single event  | Delete single event
@api_view(['GET', 'PUT', 'DELETE'])
def events_detail(request, id, format=None):

  try:
    target_event = Event.objects.get(id=id)
  except ObjectDoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = EventSerializer(target_event)
    return Response(serializer.data, status=status.HTTP_200_OK)

  elif request.method == "PUT":
    serializer = EventSerializer(target_event, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else: 
      return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == "DELETE":
    target_event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Read all Questions | Create Single Question
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated|WriteOnly])
def questions_list(request, format=None):
  if request.method == 'GET':
    allQuestions = Question.objects.all()
    serializer = QuestionSerializer(allQuestions, many=True)
    return Response(serializer.data)


  if request.method == 'POST':
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


#Get single question | Update single question | Delete single question
@api_view(['GET', 'PUT', 'DELETE'])
def questions_detail(request, id, format=None):
  try:
    target_question = Question.objects.get(id=id)
  except ObjectDoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = QuestionSerializer(target_question)
    return Response(serializer.data, status=status.HTTP_200_OK)

  elif request.method == "PUT":
    serializer = QuestionSerializer(target_question, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else: 
      return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == "DELETE":
    target_question.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Get Questions Belonging to A Single Event
@api_view(['GET'])
def questions_by_eventId(request, format=None):
  if request.data['eventId']:
    eventQuestions = Question.objects.filter(parentEvent = request.data['eventId'])
  
  if request.method == "GET":
    if len(eventQuestions) < 1:      # type: ignore
      return Response(status=status.HTTP_404_NOT_FOUND)
    else:
      serializer = QuestionSerializer(eventQuestions, many=True)        # type: ignore
      return Response(serializer.data)

