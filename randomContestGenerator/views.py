from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from . import services
# Create your views here.


class Index(TemplateView):
    template_name = 'base.html'


class RandomContest(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contest = services.GrabingJSON()
        context['contest'] = contest.grabContest('3')
        return context
