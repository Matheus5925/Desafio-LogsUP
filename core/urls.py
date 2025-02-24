"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import register_view, list_products, login_view, ProductViewSet, delete_product, product_create, change_product, home, logout_view
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", register_view, name="register"),
    path("home/", home, name="home"),
    path("products/", list_products, name="products"),
    path("products/edit/<int:product_id>/", change_product, name="product_edit"),
    path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
    path("products/create", product_create, name="product_create"),
    path("", login_view, name="login"),
    path('logout/', logout_view, name='logout'),  # A URL do logout
    path('api/v1/', include(router.urls)),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Gera o JWT
]
