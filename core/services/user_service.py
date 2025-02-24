from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

class UserService:

  @staticmethod
  def register(form_data_user, request):
    user = form_data_user.save(commit=False)
    user.save()
    print(user)
    default_group, created = Group.objects.get_or_create(name="CLIENTS")
    user.groups.add(default_group)
    teste = login(request, user)
    print(teste)
    return redirect("home")

  @staticmethod
  def login(form_data_user, request):
    username = form_data_user.cleaned_data["username"]
    password = form_data_user.cleaned_data["password"]
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        messages.success(request, "Login realizado com sucesso!")
        return redirect("home")  # Redirecionar para a página inicial ou dashboard
    else:
        messages.error(request, "Usuário ou senha inválidos")
        return redirect("login")
