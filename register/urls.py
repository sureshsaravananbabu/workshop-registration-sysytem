from django.conf.urls import url
from register import views

urlpatterns=[
    url(r'^$',views.registerr),
    url('registered/',views.index),
    url('(?P<courseid>.*)/',views.registerr),
]