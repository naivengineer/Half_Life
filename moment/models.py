from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=200)
    pass_word = models.CharField(max_length=200)
    e_mail = models.CharField(max_length=200)
    def __str__(self):
        return self.user_name
          
class Moment(models.Model):
    moment_id = models.IntegerField(default=0)
    moment_date = models.DateTimeField('date published')
    moment_text = models.CharField(max_length=2000)
    
class Message(models.Model):
    message_id = models.IntegerField(default=0)
    message_from = models.IntegerField(default=0)
    message_to = models.IntegerField(default=0)
    message_text = models.CharField(max_length=2000)
    
class user_info(models.Model):
    user_info_id = models.IntegerField(default=0)
    sex = models.CharField(max_length=2)
    birthday = models.DateTimeField('date published')
    hometown = models.CharField(max_length=200)
    
    
    