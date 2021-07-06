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
            'url': "https://codeforces.com/contestRegistration/{}/virtual/true".format(temp[0]), 'name': temp[1], 'id': temp[0]}
        return contest

    def has_participated(self, handle='fazle_rabbi_ferdaus', contest_id=''):
        if not contest_id:
            return True
        api_url = 'https://codeforces.com/api/contest.status?contestId={}&handle={}&from=1&count=1000'.format(
            contest_id, handle)
        participated_resposeJSON = requests.get(api_url).json()
        if participated_resposeJSON['result']:
            return True
        else:
            return False
