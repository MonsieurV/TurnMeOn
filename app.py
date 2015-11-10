from flask import Flask, render_template, request
import pifacedigitalio
app = Flask(__name__)
pifacedigital = pifacedigitalio.PiFaceDigital()

@app.route("/hello")
def hello2():
    return "Hello World!"

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        if request.form['submit'] == 'omg':
            pifacedigital.relays[1].turn_on()
        elif request.form['submit'] == 'miamia':
            pifacedigital.relays[1].turn_off()
    return render_template('index.html', isOn=pifacedigital.relays[1].value)

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
