from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def league(request):
    template = loader.get_template('event/league.html')
    context = {}
    return HttpResponse(template.render(context, request))
