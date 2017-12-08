from flask import Flask, request, json
from flask import render_template, jsonify
from flask import make_response
from flask import abort
# pip install requests <-- to import the library
import requests
import simplejson
import json

app = Flask(__name__) 

@app.route("/")
def hello():
    return "Hello World! - Meet | Method used: %s" % request.method

@app.route("/authors", methods=['GET', 'POST'])
def authors():
    uri = "https://jsonplaceholder.typicode.com/users"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    str1 = ""

    #for d in data:
    	#str1 += d['name'] + "<br>"

    uR = requests.get("https://jsonplaceholder.typicode.com/posts")
    data2 = json.loads(uR.text)

    for d3 in data:
	    d3['postcount'] = 0

    for d1 in data2:
    	for d2 in data:
    		if d1['userId'] == d2['id']:
    			d2['postcount'] += 1

    str1 += "author" + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + "count" + "<br>"

    for d4 in data:
    	str1 += d4['name'] + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + str(d4['postcount']) + "<br>"

    return str1


@app.route('/setcookie')
def setcookie():
    response = make_response('Setting cookie!')
    response.set_cookie("meet", "21")
    return response

@app.route('/getcookies')
def getcookie():
    cookievalue = request.cookies.get('meet')
    return cookievalue

@app.route('/robots.txt')
def limit_remote_addr():
    if request.remote_addr != '127.0.0.1':
    	#abort(403)
    	v1 = requests.get("http://httpbin.org/deny")
    	return "<pre>" + v1.text + "</pre>"
    else:
    	return render_template('robots.txt')


@app.route('/html')
def html():
	return render_template('author.html')

@app.route('/image')
def image():
	return render_template('panorama.jpg')

if __name__ == "__main__":
    app.run()
