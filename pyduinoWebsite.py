# http://www.instructables.com/id/Controlling-Arduino-with-python-based-web-API-No-p/

import flask
from pyduino import *
import time
import firebase_admin
from firebase_admin import db

app = flask.Flask(__name__)

# set up firebase
firebase_admin.initialize_app(options={
    'databaseURL': 'https://simba-282ca.firebaseio.com/'
})
READINGS = db.reference('Readings')

# initialize connection to Arduino
# if your arduino was running on a serial port other than '/dev/ttyACM0/'
# declare: a = Arduino(serial_port='/dev/ttyXXXX')
a = Arduino(serial_port='COM3')
time.sleep(3)

# declare the pins we're using
LED_PIN = 10
ANALOG_PIN_TEMP = 1
ANALOG_PIN_LIGHT = 0

# initialize the digital pin as output
a.set_pin_mode(LED_PIN,'O')

print('Arduino initialized')

# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/', methods = ['POST','GET'])
def hello_world():

    # variables for template page (templates/index.html)
    author = "Juke"

     # read in analog value from photoresistor
    readLight = a.analog_read(ANALOG_PIN_LIGHT)
    lightVal = 100*(readLight/1023.0)

    # read in analog value from temperature sensor
    readTemp = a.analog_read(ANALOG_PIN_TEMP)
    tempVoltage = readTemp * (5.0/1024.0)
    tempCelcius = (tempVoltage - 0.5) * 100
    tempFahrenheit = tempCelcius * (9.0/5.0) + 32.0

    # if we make a post request on the webpage aka press button then do stuff
    if flask.request.method == 'POST':

        # if we press the turn on button
        if flask.request.form['submit'] == 'Turn On': 
            print('Turn ON')
    
            # turn on LED on arduino
            a.digital_write(LED_PIN,0)
            
        # if we press the turn off button
        elif flask.request.form['submit'] == 'Turn Off': 
            print('Turn OFF')

            # turn off LED on arduino
            a.digital_write(LED_PIN,1)
        elif flask.request.form['submit'] == 'Upload Reading':
            print('Upload Reading')
            
            # if we press the upload reading button
            create_reading(lightVal, tempFahrenheit)
        else:
            pass
    tempVoltage = readTemp * (5.0/1024.0)

    tempCelcius = (tempVoltage - 0.5) * 100

    tempFahrenheit = tempCelcius * (9.0/5.0) + 32.0

    # the default page to display will be our template with our template variables
    return flask.render_template('index.html', author=author, lightValue = lightVal, tempValue = tempFahrenheit,)

# update firebase with temperature and light readings
def create_reading(lightVal, tempFahrenheit):
    data_ref = READINGS.child("data")
    data_ref.set({
        'temperature': {
            'temperature': str(tempFahrenheit),
            'light': str(lightVal)
        }
    })
    return

# @app.route('/heroes', methods=['POST'])
# def create_reading():
#     req = flask.request.json
#     hero = READINGS.push(req)
#     return flask.jsonify({'id': hero.key}), 201

# @app.route('/heroes/<id>')
# def read_reading(id):
#     return flask.jsonify(_ensure_hero(id))

# @app.route('/heroes/<id>', methods=['PUT'])
# def update_hero(id):
#     _ensure_hero(id)
#     req = flask.request.json
#     READINGS.child(id).update(req)
#     return flask.jsonify({'success': True})

# @app.route('/heroes/<id>', methods=['DELETE'])
# def delete_hero(id):
#     _ensure_hero(id)
#     READINGS.child(id).delete()
#     return flask.jsonify({'success': True})

# def _ensure_hero(id):
#     hero = READINGS.child(id).get()
#     if not hero:
#         flask.abort(404)
#     return hero

if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    # app.run(host='0.0.0.0')
    app.run()