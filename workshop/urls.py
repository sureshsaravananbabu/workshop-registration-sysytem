"""workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include,url
from login import views
urlpatterns = [
    url(r'^$', views.sign),
    url(r'^login/',views.login),
    url(r'^home/(?P<username>.*)',include('home.urls')),
    url(r'^addworkshop/',include('addworkshop.urls')),
    url(r'^update/',include('updateworkshop.urls')),
    url(r'^homeuser/',include('homeuser.urls')),
    url(r'^register/',include('register.urls')),
    url(r'^viewpart/(?P<courseidd>.*)',include('viewpart.urls')),
    path('admin/', admin.site.urls),
]
