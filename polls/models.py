from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Environment(models.Model):
    temperature=models.FloatField(null=True, blank=True, default=None)
    humidity=models.FloatField(null=True, blank=True, default=None)
    wind_speed=models.FloatField(null=True, blank=True, default=None)
    wind_direction=models.FloatField(null=True, blank=True, default=None)
    light=models.FloatField(null=True, blank=True, default=None)
    soid_temperature=models.FloatField(null=True, blank=True, default=None)
    soid_humidity=models.FloatField(null=True, blank=True, default=None)
    product_name = models.CharField(max_length=200,default=None)
    record_date = models.DateTimeField(default=None)




# from polls.models import Question, Choice,Environment
# from django.utils import timezone
# c = Environment(temperature='18.33',humidity='2.5',wind_speed='11.0',wind_direction='2.0',light='11.0',soid_temperature='2.0',soid_humidity='11.0',product_name='rice2',record_date=timezone.now())
# c.save()