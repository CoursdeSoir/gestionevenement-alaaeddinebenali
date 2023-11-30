from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .models import Event
from .forms import AddEventForm


# Create your views here.

def hello(request, name):
    text = F"{name}"
    return render(request, 'Event/list.html', {'name': text})


def list_events(request):
    # list = Event.objects.filter(state=True).order_by('evt_date')
    list = Event.objects.filter(state=True).order_by('-evt_date')

    nbr_event = Event.objects.count()

    return render(request, 'Event/list.html', {'events': list, "total_events": nbr_event})


class ListEvents(ListView):
    model = Event
    template_name = "Event/list.html"
    context_object_name = "events"  # same name as context render variabels

    def get_context_data(self, **kwargs):
        nbr_event = Event.objects.count()
        context = super(ListEvents, self).get_context_data(**kwargs)
        context['total_events'] = nbr_event
        return context


def detailsEvent(req, idEvent):
    try:
        event = Event.objects.get(id=idEvent)
    except Event.DoesNotExist:
        event = False

    context = {'event': event}

    return render(req, 'Event/details.html', context)


class detailsEventClass(DetailView):
    model = Event
    template_name = "Event/details.html"
    context_object_name = "event"


def addEvent(request):
    form = AddEventForm()

    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
        return redirect('classListEvent')

    return render(request, "Event/add.html", {'form': form})


class addEventClass(CreateView):
    model = Event
    template_name = "Event/add.html"
    form_class = AddEventForm()


class deleteViewClass(DeleteView):
    model= Event
    template_name = "Event/delete.html"
    success_url= reverse_lazy('classListEvent')
