from django.conf.urls import url
from addworkshop import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'addworkshop/',views.addworkshop_download)
]