from django.contrib import admin
from .models import Note, Calendar

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

class CalendarAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

admin.site.register(Note, NoteAdmin)
admin.site.register(Calendar, CalendarAdmin)