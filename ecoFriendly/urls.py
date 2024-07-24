"""
URL configuration for ecoFriendly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from EcoFriendlyProducts.views import user_login
import EcoFriendlyProducts

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('accounts/login/', EcoFriendlyProducts.views.user_login, name='login'),  # Default login view
                  path('home/', EcoFriendlyProducts.views.main, name='home'),
                  path('', EcoFriendlyProducts.views.main, name='main'),
                  path('viewAllProducts/', EcoFriendlyProducts.views.viewAllProducts, name='view-all-products'),
                  path('register/', EcoFriendlyProducts.views.register, name='register'),
                  path('login/', EcoFriendlyProducts.views.user_login, name='login'),
                  path('logout/', EcoFriendlyProducts.views.user_logout, name='logout'),
                  path('add-product/', EcoFriendlyProducts.views.add_product, name='add-product'),
                  path('modify-product/<int:product_id>/', EcoFriendlyProducts.views.modify_product,
                       name='modify-product'),
                  path('delete-product/<int:product_id>/', EcoFriendlyProducts.views.delete_product,
                       name='delete-product'),
                  path('products/', EcoFriendlyProducts.views.product_list, name='product_list'),
                  path('product/<int:product_id>/', EcoFriendlyProducts.views.product_detail, name='product_detail'),
                  path('product/<int:product_id>/add_review/', EcoFriendlyProducts.views.add_review, name='add_review'),
                  path('password_reset/', EcoFriendlyProducts.views.forgot_password, name='password_reset'),
                  path('forgot_password/', EcoFriendlyProducts.views.forgot_password_view, name='forgot_password_view'),
                  path('testpage', EcoFriendlyProducts.views.testPage, name='test'),
                  path('shop/', EcoFriendlyProducts.views.shop, name='shop'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
