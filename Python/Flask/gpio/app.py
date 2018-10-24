from flask import Flask, render_template, request, send_from_directory
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "POST":
		print request.form
		msg = request.form.get("submitBtn")
		if msg == "blue led":
			if GPIO.input(17):
				GPIO.output(17,GPIO.LOW)
			else:
				GPIO.output(17,GPIO.HIGH)
		if msg == "red led":
			if GPIO.input(18):
				GPIO.output(18,GPIO.LOW)
			else:
				GPIO.output(18,GPIO.HIGH)
	else:
		msg = "No click yet."
	return render_template("index.html", msg=msg)

@app.route('/pups/')
def pic():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'twopups.jpg',mimetype='image/jpeg')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
