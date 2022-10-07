# from django.core.exceptions import ObjectDoesNotExist
# from .models import Event, Question
# from .serializers import EventSerializer, QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])

def login(request):
  return Response(status=status.HTTP_204_NO_CONTENT)

