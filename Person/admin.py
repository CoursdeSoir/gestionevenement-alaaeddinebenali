from django.contrib import admin
from .models import Person

# Register your models here.
#admin.site.reegister(Person)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass