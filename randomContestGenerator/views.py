from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.generic import TemplateView
from . import services
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

state = {'id': '', 'url': '#',
         'name': 'Generate Todays Contest', 'status': False}

problem_state = False
todays_problem = []
saved_problem_struct = []
saved_problem_struct_state = False


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


class Allcontest(TemplateView):
    template_name = 'allcontest.html'

    def get_context_data(self, **kwargs):
        global state
        context = super().get_context_data(**kwargs)
        contest = services.GrabingJSON()
        context['contest'] = contest.grabAllcontest()
        return context


class CustomeProblems(TemplateView):
    template_name = 'customeproblems.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contest = services.GrabingJSON()
        context['problems'] = [{'url': "#", 'name': ""}]
        context['state'] = False
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


def generate_custome_contest(request):
    context = {'problems': [], 'state': False}
    if request.method == "POST":
        problemset_finder = services.GrabingJSON()
        num = int(request.POST.get('num'))
        print("custome_contest_form")
        index = []
        for i in range(1, num+1):
            index.append(request.POST.get(str(i)))
        print(*index)
        problem_set = problemset_finder.grabCustomeProblemSet(num, index)
        context = {'problems': problem_set, 'state': True}
        return render(request, "customeproblems.html", context=context)


def set_custome_problemset_struct(request):
    saved_problem_struct_state = True
    saved_problem_struct = list(map(str, range(1, 11)))
    return render(request, "customeproblems.html")


def interview_set(request):
    url = "#"
    count = 0
    complete = 0
    index = []
    return
