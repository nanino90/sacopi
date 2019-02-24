#!/usr/bin/python

from flask import Flask, render_template
import datetime
import sys
sys.path.insert(0, 'libLGTV_serial')
from libLGTV_serial import LGTV

#TV INIT
model = '42LK450'
serial_port = "/dev/ttyUSB0"
tv = LGTV(model, serial_port)
#SERVER INIT
app = Flask(__name__)

@app.route('/')
def index():
	now = datetime.datetime.now()
   	timeString = now.strftime("%Y-%m-%d %H:%M")
   	templateData = {
      		'title' : 'HELLO!',
      		'time': timeString
      		}

   	return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>", methods=['GET'])
def action(deviceName, action):
	if deviceName == 'TV':
		if action == "on":
			print "tv on"
                        tv.send("poweron")
		if action == "off":
			print "tv off"
                        tv.send("poweroff")
		if action == "mute":
			print "mute"
                        tv.send("togglemute")
                if action == "RPI":
			print "Input RPI"
                        tv.send("inputhdmi1")
		if action == "tv":
			print "input tv"
                        tv.send("inputdigitalantenna")
		if action == "up":
			print "volume up"
                        tv.send("volumeup")
		if action == "down":
			print "volume down"
                        tv.send("volumedown")

	return render_template('index.html')
		     
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
