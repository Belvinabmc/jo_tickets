from django.contrib import admin
from .models import Team, Stadium, Event
from .models import Team, Stadium, Event, Ticket

admin.site.register(Team)
admin.site.register(Stadium)
admin.site.register(Event)
admin.site.register(Ticket)