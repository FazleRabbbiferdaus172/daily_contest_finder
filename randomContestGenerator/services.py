import requests
import json
import random
from django.core import serializers
from collections import defaultdict


class GrabingJSON:

    def grabContest(self, t):
        resposeJSON = requests.get(
            'https://codeforces.com/api/contest.list?gym=false').json()
        contest_type = 'Div. ' + t
        all = []
        for i in resposeJSON['result']:
            if contest_type in i['name'] and i['phase'] == "FINISHED":
                all.append((i['id'], i['name']))
        temp = random.choice(all)
        # contest = {
        #     'url': "https://codeforces.com/contestRegistration/{}/virtual/true".format(temp[0]), 'name': temp[1], 'id': temp[0]}

        contest = {
            'url': "https://codeforces.com/contest/{}".format(temp[0]), 'name': temp[1], 'id': temp[0]}

        return contest

    def grabAllcontest(self, t='3'):
        resposeJSON = requests.get(
            'https://codeforces.com/api/contest.list?gym=false').json()
        contest_type = 'Div. ' + t
        all = []
        for i in resposeJSON['result']:
            if contest_type in i['name'] and i['phase'] == "FINISHED":
                all.append(
                    {'url': 'https://codeforces.com/contest/{}'.format(i['id']), 'name': i['name']})
        # print(all)

        return all

    def grabCustomeProblemSet(self, number=3, index=['A']):
        api_url = 'https://codeforces.com/api/problemset.problems'
        all = defaultdict(list)
        all_index = defaultdict(int)
        for i in index:
            all_index[i] += 1
        problem_set_responseJSON = participated_resposeJSON = requests.get(
            api_url).json()
        c = 0
        for i in problem_set_responseJSON['result']['problems']:
            all[i["index"]].append({'url': 'https://codeforces.com/problemset/problem/{}/{}'.format(
                i["contestId"], i["index"]), 'name': i['name']})
        random.shuffle(all)
        # print(all['A'])
        send_these_problems = []
        for i in all_index:
            random.shuffle(all[i])
            send_these_problems.extend(all[i][:all_index[i]])
        # print(send_these_problems)
        return send_these_problems

    def has_participated(self, handle='', contest_id=''):
        if not contest_id:
            return True
        api_url = 'https://codeforces.com/api/contest.status?contestId={}&handle={}&from=1&count=1000'.format(
            contest_id, handle)
        participated_resposeJSON = requests.get(api_url).json()
        if participated_resposeJSON['result']:
            return True
        else:
            return False


# temp = GrabingJSON().grabCustomeProblemSet()
