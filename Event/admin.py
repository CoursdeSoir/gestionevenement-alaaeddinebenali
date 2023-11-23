from django.contrib import admin

from Event.models import Participants, Event


# Register your models here.
@admin.register(Event, Participants)
class EventAdmin(admin.ModelAdmin):
    pass
