import requests
import json
import random


class GrabingJSON:
    def __init__(self):
        self.resposeJSON = requests.get(
            'https://codeforces.com/api/contest.list?gym=false').json()

    def grabContest(self, t):
        contest_type = 'Div. ' + t
        all = []
        for i in self.resposeJSON['result']:
            if contest_type in i['name'] and i['phase'] == "FINISHED":
                all.append((i['id'], i['name']))
        temp = random.choice(all)
        contest = {
            'url': "https://codeforces.com/contestRegistration/1542/virtual/true".format(temp[0]), 'name': temp[1]}
        return contest
