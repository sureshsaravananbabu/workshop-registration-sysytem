from django.conf.urls import url
from updateworkshop import views
urlpatterns=[
 url(r'^$',views.update),
 url('updated/',views.index),
 url('(?P<courseid>.*)/(?P<professor>.*)/(?P<timings>.*)/(?P<maxstrength>.*)/(?P<title>.*)/(?P<description>.*)/',views.update)
]