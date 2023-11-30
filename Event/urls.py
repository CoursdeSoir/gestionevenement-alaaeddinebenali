from django.urls import path
from .views import hello, list_events, ListEvents

urlpatterns = [
    path('bonjour/<str:name>', hello),
    path('list', list_events),
    path('listEvent', ListEvents.as_view()),
]
