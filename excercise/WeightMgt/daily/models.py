from django.db import models
from user.models import User

# Create your models here.
class DailyMeasurement(models.Model):
    def __str__(self):
        return self.created_date
    user_id = models.ForeignKey(User)
    weight = models.FloatField()
    bodyfat = models.FloatField()
    innerfat = models.FloatField()
    basal_metabolism = models.IntegerField()
    body_age = models.IntegerField()
    modified_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)