from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from . import services
# Create your views here.

state = {'id': '', 'url': '#',
         'name': 'Generate Todays Contest', 'status': False}


class Index(TemplateView):
    template_name = 'index.html'


class RandomContest(TemplateView):
    template_name = 'randomContest.html'

    def get_context_data(self, **kwargs):
        global state
        context = super().get_context_data(**kwargs)
        context['contest'] = {
            'url': state['url'], 'name': state['name'], 'id': state['id']}
        return context


def generate_random_contest(request):
    global state
    if request.method == "POST":
        contest = services.GrabingJSON()
        contest_type = request.POST.get('size')
        print(type(contest_type))
        if not contest_type:
            contest_type = '3'
        if state['status'] or contest.has_participated(handle='fazle_rabbi_ferdaus', contest_id=state['id']):
            context = {'contest': contest.grabContest(contest_type)}
            state['id'] = context['contest']['id']
            state['url'] = context['contest']['url']
            state['name'] = context['contest']['name']
            state['status'] = contest.has_participated(
                handle='fazle_rabbi_ferdaus', contest_id=state['id'])
            # print(state)

        else:
            context = {'contest': {
                'url': state['url'], 'name': state['name'], 'id': state['id']}}

        return render(request, "randomContest.html", context=context)
