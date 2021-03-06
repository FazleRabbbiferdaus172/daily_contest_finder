"""dailyRandomContest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from randomContestGenerator.views import (
    Index, RandomContest, generate_random_contest, Allcontest, CustomeProblems, generate_custome_contest, set_custome_problemset_struct, interview_set)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RandomContest.as_view(), name='index'),
    url(r'^randomcontest', RandomContest.as_view(), name='randomcontest'),
    url(r'^all_contest', Allcontest.as_view(),
        name='all_contest'),
    url(r'^custome_problems', CustomeProblems.as_view(),
        name='custome_problems'),
    url(r'^generate_random_contest', generate_random_contest,
        name='generate_random_contest'),
    url(r'^generate_custome_contest', generate_custome_contest,
        name='generate_custome_contest'),
    url(r'^set_custome_problemset_struct', set_custome_problemset_struct,
        name='set_custome_problemset_struct'),
]
