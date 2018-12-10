from django.db import models

# Create your models here.
class Student(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    grade = models.IntegerField(default=1)
    register = models.DateField(auto_now_add=True)

class Classroom(models.Model):
    def __str__(self):
        return self.room_number
    room_number = models.CharField(max_length=20)
    room_capacity = models.IntegerField(default=40)
    updated = models.DateTimeField(auto_now=True,null=True)

class Classes(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    weekday = models.IntegerField(default=0)
    period = models.TimeField(null=True)
    periodend = models.TimeField(null=True)
    updated = models.DateTimeField(auto_now=True,null=True)