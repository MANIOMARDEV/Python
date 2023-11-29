#this waas before
# from django.shortcuts import render

# # Create your views here.

#this is after
from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def redirecting_method(request):
    return redirect("/blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request, number):
    return HttpResponse("placeholder to display blog number %s." % number) # % and number should be separated by a space
def edit(request, number):
    return HttpResponse("placeholder to edit blog %s." % number)
def destroy(request, number):
    return redirect("/blogs")
def myjson(request):
    return JsonResponse({"title":"this is json","description":"nothing important","response": "JSON response from redirected_method", "status": True})