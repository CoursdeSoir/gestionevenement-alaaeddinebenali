from django.forms import ModelForm
from .models import Event
class AddEventForm(ModelForm):
    class Meta:
        model= Event
        # All fields
        #fields = "__all__"
        # Specific fields
        #fields = ('title')
        exclude= ('state','nbr_participants')
