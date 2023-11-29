from django.shortcuts import render, redirect
from . import models

# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        if request.POST["login_type"] == "login":
            if models.check_user(
                request.POST["user_name"]): request.POST["password"]
            request.session["user_name"] = request.POST["name"]
            return render(request, "welcome.html")



        if request.POST["login_type"] == "registration":
            models.register(request.POST["name"], request.post["password"])

    return redirect("/")
