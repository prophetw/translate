from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    question=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question   # __unicode__ on Python 2
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question=models.ForeignKey(Question)
    choice=models.CharField(max_length=200)
    votes=models.IntegerField()
    def __str__(self):
        return self.choice    # __unicode__ on Python 2
