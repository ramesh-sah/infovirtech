"""
URL configuration for infovirtech project.

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
from infovirtech import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name="index"),
    path("home/",views.home, name="Home"),
    path("about/",views.about,name="about"),
    path("services/",views.services,name="service"),
    path("contacts/",views.contacts,name="contact"),
    path("sign-up/", views.signup),
    path("Login/",views.logiN),
    path("Logout/",views.logouT)
]
