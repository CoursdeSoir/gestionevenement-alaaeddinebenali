from django.contrib import admin, messages

from .models import Participants, Event
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

def accept_state(ModelAdmin,request, queryset):
    row_updated = Event.objects.update(state=True)
    #row_updated = Event.filter(state=True).delete();

    if (row_updated == 1):
        msg = " 1 event was"
    else:
        msg = F"{row_updated} event were"

    messages.success(request, F'{msg} successfully updated')

def refuse_state(ModelAdmin,request, queryset):
    row_updated = Event.objects.update(state=False)

    if (row_updated == 1):
        msg = " 1 event was"
    else:
        msg = F"{row_updated} event were"

    messages.success(request, F'{msg} successfully updated')


# Register your models here.
accept_state.short_description = "State True"
refuse_state.short_description = "State False"


class ParticipationInline(admin.TabularInline):
    model = Participants
    extra = 1
    readonly_fields = ('participation_date',)
    classes = ['collapse']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'evt_date', 'state', 'nbr_participants', 'numberOfParticipants')

    readonly_fields = ('created_at', 'updated_at')

    def numberOfParticipants(self, obj):
        nb = obj.participant.count()
        return nb

    list_per_page = 2
    list_filter = ('title', nbr_participants, eventDate,)
    autocomplete_fields = ['organisateur']
    actions = [accept_state,refuse_state]

    fieldsets = (
        ('A propos', {"fields": ('title', 'description', 'image'), }),
        ('Date', {"fields": ('evt_date', 'created_at', 'updated_at')
                  }),
        ('Others', {"fields": ('category', 'state', 'nbr_participants')}),
        ('Personal', {"fields": ('organisateur',)}))

    inlines = [ParticipationInline]


@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    pass
