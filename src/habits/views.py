import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from rest_framework import viewsets
from rest_framework import permissions

from .models import Habit
from .serializers import HabitSerializer


def create_habit(request):
    if request.method == 'POST':
        if 'title' in request.POST:
            title = request.POST['title']
            habit = Habit.create(title=title)
            return redirect('habits:view_habit', id=habit.id)
        else:
            return HttpResponse("<h2> Bad Request </h2>")

    return redirect('home')


def view_habit(request, id):
    habit = Habit.objects.get(id=id)
    habit_json_url = json.dumps(reverse('habit-detail', args=[habit.id]))
    return render(request, 'habits/habit_detail.html', {'habit_json_url': habit_json_url})


class HabitViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
