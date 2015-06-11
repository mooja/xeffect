from django.views import generic


class CreateHabit(generic.TemplateView):
    template_name = "home.html"
