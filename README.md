# FacebookGraphApi

In this respository it contains multiple miniproject which uses a Facebook Graph API.

1 ) Bday_Reply_Msg.py

A python application which comment and like for b'day wishes on my facebook account.
It Uses a Facebook Graph Api i.e facepy,"request" for making GET and POST request to facebook.

To use this application please install its dependencies i.e facepy,simplejson,requests.

Generate your access_token from developer facebook site and put it in the code.


Useful links :
https://facepy.readthedocs.org/en/latest/
https://developers.facebook.com/docs/reference/fql/stream/
https://developers.facebook.com/docs/graph-api/reference/v2.3/object/likes
http://www.sitepoint.com/2-cool-things-can-facebook-graph-api/
https://developers.facebook.com/docs/reference/fql/
http://www.w3programmers.com/working-with-facebook-api-part-3/
https://facepy.readthedocs.org/en/latest/usage/graph-api.html
https://developers.facebook.com/docs/graph-api/reference/v2.3/object/comments
https://developers.facebook.com/docs/graph-api/reference
http://www.pythonforbeginners.com/requests/using-requests-in-python
http://www.pythonforbeginners.com/python-on-the-web/parsingjson/

2) Frnd_Bday_Wish.py

A python application which wishes on my friend facebook account for having birthday.Generate your access_token from developer facebook site and put it in the code.

3) Vlc_Facebook_Update.py

A python application which updates a status on my facebook account when i listen to 
a song or watch a video in VLC on my local machine.It uses basically Facebook Graph Api.
Generate your access_token from developer facebook site and put it in the code.

To run this application first install its dependencies i.e urllib2,base64,xml.etree.ElementTree,facepy.

Commamd to run this application:

First run this command : vlc -I http to run vlc http server.
Then python Vlc_Facebook_Update.py




