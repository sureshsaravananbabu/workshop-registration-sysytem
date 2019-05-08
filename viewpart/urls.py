from django.conf.urls import url
from viewpart import views

urlpatterns=[
    url(r'^$',views.viewparticipant),
]