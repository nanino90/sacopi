from flask import Flask, render_template
import datetime

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

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'TV':
   
		if action == "on":
			print "tv on"
		if action == "off":
			print "tv off"
   	
	return render_template('index.html')
		     
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
