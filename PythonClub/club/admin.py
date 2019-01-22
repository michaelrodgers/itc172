from django.contrib import admin
from .models import Event, Meeting, Minutes, Resource

# Register your models here.
admin.site.register(Event)
admin.site.register(Meeting)
admin.site.register(Minutes)
admin.site.register(Resource)
