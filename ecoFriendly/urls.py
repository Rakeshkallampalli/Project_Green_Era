from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from EcoFriendlyProducts.views import user_login
import EcoFriendlyProducts

urlpatterns = [
                path("admin/", admin.site.urls),
                path('login/', EcoFriendlyProducts.views.user_login, name='login'),
                path('logout/', EcoFriendlyProducts.views.user_logout, name='logout'),
              ]
