import urllib2
import base64
import xml.etree.ElementTree as ET
from facepy import GraphAPI

def facebook_post(file_name,opt):
	access_token=''
	graph=GraphAPI(access_token)
	if opt==1:
		msg='Watching '+file_name+' on VLC Media Player'
	else:
		msg='Listening to '+file_name+' on VLC Media Player'
	print msg
	graph.post('me/feed',message=msg)


def file_name_from_vlc_server():
	print "VLC monitor exiting..."
	audio_extensions = ['mp3', 'wav','MP3','WAV']
	video_extensions = ['mp4', 'flv', 'mov', 'mkv', 'avi','MP4', 'FLV', 'MOV', 'MKV', 'AVI']

	request=urllib2.Request('http://localhost:8080/requests/status.xml')
	encoded = base64.encodestring('%s:%s'%('','poppy'))

	request.add_header("Authorization","Basic "+ encoded)
	result = urllib2.urlopen(request)
	cntnt = result.read()

	root=ET.fromstring(cntnt)

	file_info=root.find('information')

	myfile_status=0
	type_status=0

	for info in file_info:
		if info.get('name')=='meta':
			for get_file in info:
				if get_file.get('name')=='filename':
					myfile_status=1
					file_name=get_file.text
		if info.get('name')=='Stream 0':
			for type_file in info:
				if type_file.get('name')=='Type':
					Type=type_file.text

	if myfile_status==0:
		print "Nothing is played"
	else:
		work_status=0

		for ext in audio_extensions:
			if file_name.find(ext) >= 0:
				work_status=1
				facebook_post(file_name,0)


		if work_status==0:
			for ext in video_extensions:
				if file_name.find(ext) >=0:
					work_status=1
					facebook_post(file_name,1)

		if work_status==0:
			if Type=='Video':
				facebook_post(file_name,1)
			else:
				facebook_post(file_name,0)


if __name__ == "__main__":

	file_name_from_vlc_server()
