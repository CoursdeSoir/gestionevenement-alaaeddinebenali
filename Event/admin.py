from django.contrib import admin

from Event.models import Participants, Event
from datetime import datetime


class nbr_participants(admin.SimpleListFilter):
    title = "Nbre of participants"
    parameter_name = "nbr_participants"

    def lookups(self, request, model_admin):
        return (
            ('No', ('No Participants')),
            ('Yes', ('There are participants'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'No':
            return queryset.filter(nbr_participants__exact=0)
        if self.value() == 'Yes':
            return queryset.filter(nbr_participants__gt=0)

class eventDate(admin.SimpleListFilter):
    title = "Date of event"
    parameter_name = "evt_date"

    def lookups(self, request, model_admin):
        return (
            ('Tomorrow', ('Upcomming Events')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Tomorrow':
            return queryset.filter(evt_date__gt=datetime.now())


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'evt_date', 'state', 'nbr_participants' ,'numberOfParticipants')

    readonly_fields = ('created_at', 'updated_at')

    def numberOfParticipants(self, obj):
        nb = obj.participant.count()
        return nb

    list_per_page = 2
    list_filter = ('title', nbr_participants,eventDate,)


@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    pass
