from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Habit


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
    return HttpResponse("<h3> habit id: {} </h3>".format(str(id)))
