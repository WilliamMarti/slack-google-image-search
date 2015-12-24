import os
import urllib2
from flask import Flask, jsonify, request
from google import google, images
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['POST'])
def returnJson():
	#make json
	#request.query_string
	request_data = request.form.get('text')
	imageUrl = getImage(request_data)
	#return it
	return jsonify(response_type='in_channel',text=imageUrl)
	#return jsonify(response_type='in_channel',text=imageUrl)

def getImage(request_data):
	options = images.ImageOptions()
	options.image_type = images.ImageType.gif
	results = google.search_images(request_data, options)
	#goog_results = goog_results.json()
	#imageUrl = goog_results
	return results