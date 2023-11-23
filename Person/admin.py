from django.contrib import admin
from .models import Person

# Register your models here.
#admin.site.reegister(Person)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("username","email","cin","last_login")
    search_fields = ["username"]