from django.conf.urls import url

from .views import create_habit, view_habit
# from .views import ViewHabit

urlpatterns = [
    url(r'^$', create_habit, name='create_habit'),
    url(r'^(?P<id>\w{20})$', view_habit, name='view_habit'),
]
