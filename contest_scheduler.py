import requests
import pytz
from datetime import datetime
import json


class Contest:
    def __init__(self, id, name, platform, link, startTime, endTime):
        self.id = id
        self.name = name
        self.platform = platform
        self.link = link
        self.startTime = startTime
        self.endTime = endTime



TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
epoch = datetime.utcfromtimestamp(0)

def getTimeInMillis(time_str):
    time_object = datetime.strptime(time_str, TIME_FORMAT)
    return int((time_object-epoch).total_seconds()*1000)

'''
Meta: 133
codeforces: 1
codechef: 2
leetcode: 102
google: 35
atcoder: 93
'''
def getPlatformIdFromResourceId(clistId):
    if (clistId == 1):
        return 1
    elif (clistId == 2):
        return 2
    elif (clistId == 93):
        return 3
    elif (clistId == 102):
        return 4
    elif (clistId == 35):
        return 5
    elif (clistId == 133):
        return 6
    else:
        return -1
    
def getPlatformNameFromResourceId(clistId):
    if (clistId == 1):
        return 'Codeforces'
    elif (clistId == 2):
        return 'Codechef'
    elif (clistId == 93):
        return 'Atcoder'
    elif (clistId == 102):
        return 'Leetcode'
    elif (clistId == 35):
        return 'Google'
    elif (clistId == 133):
        return 'Meta'
    else:
        return 'Platform not supported'
    

URL = "https://clist.by:443/api/v2/contest/?filtered=true&order_by=-start&limit=150&username=MaskedCarrot&api_key=3756ead7ff87d60d0029be2c4d3b6847ad6aa1b5"

data = requests.get(url = URL).json()
processedData = {'contests': []}

for d in data['objects']:    
    if (getPlatformIdFromResourceId(d['resource_id']) == -1): 
            continue
    processedData['contests'].append(
        Contest(
            id=getPlatformIdFromResourceId(d['resource_id']),
            name=d['event'],
            platform=getPlatformNameFromResourceId(d['resource_id']),
            link=d['href'],
            startTime=getTimeInMillis(d['start']),
            endTime=getTimeInMillis(d['end'])
        ).__dict__
    )
    
with open('data/contests.json', 'w') as outfile:
    json.dump(processedData, outfile, indent=4)
