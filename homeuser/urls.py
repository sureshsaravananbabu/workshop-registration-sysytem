from django.conf.urls import url
from homeuser import views
urlpatterns=[
    url(r'^$',views.homeuser),
]