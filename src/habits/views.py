from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework import viewsets

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

    return render(request, 'habits/create_habit.html')


def view_habit(request, id):
    habit = Habit.objects.get(id=id)
    return render(request, 'habits/habit_detail.html', {'habit': habit})


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
