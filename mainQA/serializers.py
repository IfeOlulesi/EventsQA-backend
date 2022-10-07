from rest_framework import serializers
from .models import Event, Question

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'name', 'eventCode', 'desc', 'dateCreated', 'createdBy', 'location', 'isAcceptingQuestions']


class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = ['id', 'questionText', 'eventCode', 'dateCreated', 'createdBy']