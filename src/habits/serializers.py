from habits.models import Habit
from rest_framework import serializers


class HabitSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Habit
        fields = ('url', 'id', 'title', 'status', 'created')
