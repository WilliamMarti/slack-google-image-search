import os
import urllib2
import simplejson
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['POST'])
def returnJson():
	#make json
	#request.query_string
	request_data = request.form.get('text')
	request_ip = request.remote_addr
	return jsonify(response_type='in_channel',text=request_ip)
	imageUrl = getImage(request_data,request_ip)
	#return it
	#return jsonify(response_type='in_channel',text=imageUrl)

def getImage(request_data,ip):
	fetcher = urllib2.build_opener()
	searchTerm = request_data
	startIndex = 0
	searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + startIndex
	url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
	       'v=1.0&q=barack%20obama&userip=' + ip)

	request = urllib2.Request(url, None, {'Referer': 'https://salty-taiga-1657.herokuapp.com/image'})
	response = urllib2.urlopen(request)

	# Process the JSON string.
	results = simplejson.load(response)
	imageUrl = results['responseData']['results'][0]['unescapedUrl']
	#file = cStringIO.StringIO(urllib.urlopen(imageUrl).read())
	return imageUrl