from flask import Flask, render_template,request, redirect, url_for
from pyduino import *
import time

app = Flask(__name__)

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

    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        # if we press the turn on button
        if request.form['submit'] == 'Turn On': 
            print('Turn ON')
    
            # turn on LED on arduino
            a.digital_write(LED_PIN,0)
            
        # if we press the turn off button
        elif request.form['submit'] == 'Turn Off': 
            print('Turn OFF')

            # turn off LED on arduino
            a.digital_write(LED_PIN,1)

        else:
            pass
    
    # read in analog value from photoresistor
    readLight = a.analog_read(ANALOG_PIN_LIGHT)

    # read in analog value from temperature sensor
    readTemp = a.analog_read(ANALOG_PIN_TEMP)

    tempVoltage = readTemp * (5.0/1024.0)

    tempCelcius = (tempVoltage - 0.5) * 100

    tempFahrenheit = tempCelcius * (9.0/5.0) + 32.0

    # the default page to display will be our template with our template variables
    return render_template('index.html', author=author, lightValue=100*(readLight/1023.), tempValue = tempFahrenheit,)

if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    # app.run(host='0.0.0.0')
    app.run()