"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('recipes/',Recipes_func,name="recipes"),
    path('delete_recipes/<id>/',delete_recipes,name="delete_recipes"),
    path('update_recipes/<id>/',update_recipes,name="update_recipes"),
    path('Login/',login_pg,name='Login'),
    path('Register/',register_pg,name='Register'),
    path('Logout/',logout_pg,name="logout_pg"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
