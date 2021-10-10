from django.contrib import admin

from authorisation.models import CustomPerson


@admin.register(CustomPerson)
class PersonUserAdmin(admin.ModelAdmin):
    pass