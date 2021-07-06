from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from . import services
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'


class RandomContest(TemplateView):
    template_name = 'randomContest.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contest'] = {
            'url': "#", 'name': "Generate Todays Contest"}
        return context


def generate_random_contest(request):
    if request.method == "GET":
        contest = services.GrabingJSON()
        context = {'contest': contest.grabContest('3')}
        return render(request, "randomContest.html", context=context)
