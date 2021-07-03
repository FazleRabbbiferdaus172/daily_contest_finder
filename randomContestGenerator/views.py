from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
import requests
# Create your views here.


class Index(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contests'] = requests.get(
            'https://codeforces.com/api/contest.list?gym=false').json()
        return context
