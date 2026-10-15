from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):                   # P12: registration (CSRF protected form)
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Account created. Please log in.")
        return redirect("login")
    return render(request, "registration/signup.html", {"form": form})
