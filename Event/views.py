from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Event


# Create your views here.

def hello(request, name):
    text = F"{name}"
    return render(request, 'Event/list.html', {'name': text})


def list_events(request, ):
    list = Event.objects.all()

    return render(request, 'Event/list.html', {'events': list})


class ListEvents(ListView):
    model = Event
    template_name = "Event/list.html"
    context_object_name = "events" # same name as context render variabels
