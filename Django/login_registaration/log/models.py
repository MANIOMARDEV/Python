from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def register(username,password): 
    Users.objects.create(username=username,password=password)



def check_user (name,password):
    user_name=Users.objects.filter(username=name)
    if user_name == None:
        return False
    if user_name.password == password:
        return True

    return False    

