from django.conf.urls import url

from .views import CreateHabit
# from .views import ViewHabit

urlpatterns = [
    url(r'^$', CreateHabit.as_view(), name='create_habit'),
]
