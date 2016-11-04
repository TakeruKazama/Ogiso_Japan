from django.shortcuts import render
from django.utils.html import mark_safe

from .models import Team, Game


def results(request, year):
    return render(request, 'soccer/results.html', {
     'game_result': Game.objects.all()
    })
