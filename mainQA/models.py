from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import string

# Create your models here.

def ec_gen():
  ec = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
  return ec


class Event(models.Model):
  name = models.CharField(max_length=50)
  eventCode = models.CharField(max_length=6, default=ec_gen)
  desc = models.CharField(max_length=300, default="")
  dateCreated = models.DateTimeField(auto_now_add=True)
  createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=100)
  isAcceptingQuestions = models.BooleanField()


  def __str__(self):
    return self.name


class Question(models.Model):
  questionText = models.TextField()
  parentEvent = models.ForeignKey(Event, on_delete=models.CASCADE)
  dateCreated = models.DateTimeField(auto_now_add=True)
  createdBy = models.CharField(default="Anonymous",max_length=100)


  def __str__(self):
    displayShort = self.parentEvent.eventCode + ": " + self.questionText[0:20] + '...'
    return displayShort