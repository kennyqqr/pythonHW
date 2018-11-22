from django.db import models

# Create your models here.
class User(models.Model):
    def __str__(self):
        return self.account

    account = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    login_ip = models.CharField(max_length=100)
    login_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)

class UserDetail(models.Model):
    def __str__(self):
        return self.name
    user_id = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    birth = models.DateField()
    height = models.FloatField()
    modified_date = models.DateTimeField(auto_now_add=True)