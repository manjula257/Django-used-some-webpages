"""
URL configuration for newprojct project.

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
from django.urls import path
from newprojctapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data',views.employeeData),
    path("",views.fetching_data),
    path('mainpage',views.mainpage,name='mainpage'),
    path('hyderabad',views.hyderabad,name='hyderabad'),
    path('banglore',views.banglore,name='banglore'),
    path('chennai',views.chennai,name='chennai'),
    path('pune',views.pune,name='pune'),
]