from django.conf.urls import url
from django.views.generic import ListView, DetailView
from team.models import Team, Match
from . import views

app_name = 'team'
urlpatterns = [
    url(r'^$', ListView.as_view(model=Team)),
    ]
