from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World! You're at the moment index.")
    
def user_check(request, user_id):
    #response = "You're looking at the result of user %s. \
    #The username is %s."
    return HttpResponse("You're looking at question %s." % user_id)
