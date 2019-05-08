from django.conf.urls import url
from login import views

urlpatterns=[
    url(r'^$',views.sign),
    url(r'login/',views.login),
]