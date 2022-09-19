from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=50)
  eventCode = models.CharField(max_length=20)
  desc = models.CharField(max_length=300)
  dateCreated = models.DateTimeField(default=timezone.now)
  createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=100)
  isAcceptingQuestions = models.BooleanField()


  def __str__(self):
    return self.name


class Question(models.Model):
  questionText = models.TextField()
  eventCode = models.ForeignKey(Event, on_delete=models.CASCADE) #this guy still points to the model, and not the event code
  dateCreated = models.DateTimeField(default=timezone.now)
  createdBy = models.CharField(default="Anonymous",max_length=100)


  def __str__(self):
    displayShort = self.eventCode.eventCode + ": " + self.questionText[0:20] + '...'
    return displayShort  #work on this and return maybe the first 30 characters followed with trailing dots...