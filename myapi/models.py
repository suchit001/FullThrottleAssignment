from django.db import models
from django.utils.datetime_safe import datetime


# MEMBER MODEL
class User(models.Model):
    real_name = models.CharField(max_length=60)
    tz = models.CharField(max_length=60)
    def __str__(self):
        return self.real_name

# ACTIVITY MODEL WITH FOREIGN KEY TO MEMBER
class Activity(models.Model):
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey('User', related_name='activity_period', on_delete = models.CASCADE)

    def __str__(self):
        return self.user.real_name
# Create your models here.
