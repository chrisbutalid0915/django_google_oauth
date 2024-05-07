from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView
from django.contrib import messages


class Login(LoginView):
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, "You have been logged in!")
            return redirect("/")
        else:
            messages.success(request, "Incorrect Username of Password.")
            return redirect("/")


def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect("/")