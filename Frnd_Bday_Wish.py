from facepy  import GraphAPI
import datetime
import requests
import json

access_token=''
graph=GraphAPI(access_token)
friend_list=graph.get("me/friends?fields=birthday,name")

msg="Happy b'day :)"

#Get today's day and month

print friend_list

now = datetime.datetime.now().strftime("%m-%d")
month_day = now.split('-')
print month_day[0] + "  "  + month_day[1] + "here1"

for friend in friend_list['data']:
    if friend.has_key('birthday'):
        bday = friend['birthday'].split('/')
        if bday[0] == month_day[0] and bday[1] == month_day[1]:
            graph.post(friend['id']+ '/feed', message = msg)
            print "Wished " + friend['name']

