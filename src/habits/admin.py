from django.contrib import admin

from .models import Habit


class HabitAdmin(admin.ModelAdmin):
    fields = ['title', 'id', 'status']
    list_display = ('created', 'title', 'id')


admin.site.register(Habit, HabitAdmin)
