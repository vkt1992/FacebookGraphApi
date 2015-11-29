from facepy import GraphAPI
import simplejson,json
import requests
from random import randint

access_token=''
AFTER = 1442664000
msg=['thanks','thanks a lot','thankyou']

query = ("SELECT post_id, actor_id, message FROM stream WHERE "

            "filter_key = 'others' AND source_id = me() AND "

            "created_time >= 1442707200 ")

payload = {'q': query, 'access_token': access_token}
r = requests.get('https://graph.facebook.com/fql', params=payload)
result = json.loads(r.text)

#print result

wallposts = result['data']

#print wallposts

for wallpost in wallposts:
	 comment_url = 'https://graph.facebook.com/%s/comments' %wallpost['post_id']
	 like_url='https://graph.facebook.com/%s/likes' %wallpost['post_id']
	  
	 pos=randint(0,2)

	 #print wallpost['message']
	 #print msg[pos]

	 payload = {'access_token': access_token, 'message': msg[pos]}
	 comment = requests.post(comment_url, data=payload)
	 payload = {'access_token': access_token}
	 like = requests.post(like_url,payload)

#unix timestamp follow ---------->  http://www.epochconverter.com/
