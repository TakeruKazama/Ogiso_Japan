from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<year>\d+)/$', views.results),
]
