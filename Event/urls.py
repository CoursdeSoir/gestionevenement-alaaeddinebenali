from django.urls import path
from .views import hello, list_events, ListEvents, detailsEvent, detailsEventClass, addEvent,deleteViewClass

urlpatterns = [
    path('bonjour/<str:name>', hello),
    path('list', list_events, name="listEvent"),
    path('listEvent', ListEvents.as_view(), name="classListEvent"),
    path('details/<int:idEvent>', detailsEvent, name="detailsEvent"),
    path('detailsEvent/<int:pk>', detailsEventClass.as_view(), name="classDetailsEvent"),
    path('update/<int:idEvent>', detailsEvent, name="updateEvent"),
    path('add', addEvent, name="addEvent"),
    path('addEvent', addEvent, name="classAddEvent"),
    path('deleteEvent/<int:pk>', deleteViewClass.as_view(), name="classDeleteEvent"),
]
