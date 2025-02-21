from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.models import User, Group
from .forms import UserRegistrationForm, LoginForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from core.services.user_service import UserService
from core.services.product_service import ProductService
from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .decorators import check_group_permission, login_required_custom
from django.contrib.auth import logout

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        name = self.request.GET.get('name', None)
        return ProductService.get_all(name)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          return UserService.register(form, request)
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return UserService.login(form, request)
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required_custom
@check_group_permission(["CLIENTS", "ANALYSTS", "SUPERVISORS"])
def list_products(request):
    if request.user.is_authenticated:
        name = request.GET.get('name', None)
        products = ProductService.get_all(name)

        return render(request, "list_products.html", {"products": products})
  
    return redirect("login")

@login_required_custom
@check_group_permission(["SUPERVISORS"])
def delete_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        product.delete()  # Deleta o produto
        return redirect('products')  # Redireciona para a página de lista de produtos

@login_required_custom
@check_group_permission(["SUPERVISORS"])
def change_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)  # Preenche o form com os dados do produto
        if form.is_valid():
            form.save()
            return redirect("products")  # Redireciona para a lista de produtos após edição
    else:
        form = ProductForm(instance=product)  # Preenche o form com os dados atuais do produto

    return render(request, "change_product.html", {"form": form})

@login_required_custom
@check_group_permission(["SUPERVISORS", "ANALYSTS"])
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.creator = request.user  # Atribui o usuário logado ao campo creator
            product.save()  #
            return redirect('products')  # Redireciona para a lista de produtos
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})

@login_required_custom
@check_group_permission(["CLIENTS", "ANALYSTS", "SUPERVISORS"])
def home(request):
    return render(request, "home.html")