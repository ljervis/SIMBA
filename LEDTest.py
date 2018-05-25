from pyduino import *
import time

if __name__ == '__main__':
    
    a = Arduino(serial_port='COM3')
    # if your arduino was running on a serial port other than '/dev/ttyACM0/'
    # declare: a = Arduino(serial_port='/dev/ttyXXXX')

    time.sleep(3)
    print('Established connection to the ardino')
    # sleep to ensure ample time for computer to make serial connection 

    PIN9 = 9
    PIN10 = 10
    PIN11 = 11
    # a.set_pin_mode(PIN9,'O') # red
    a.set_pin_mode(PIN10,'O') # green
    # a.set_pin_mode(PIN11,'O') # blue

    time.sleep(1)

    a.digital_write(PIN10, 1) # turn on pin 

    for i in range(0,1000):

        try:
            # Read the analog value from analogpin 0
            analog_val = a.analog_read(0)
            
            # print value in range between 0-100
            print('ANALOG READ =',int((analog_val/1023.)*100))
            time.sleep(1)

        except KeyboardInterrupt:   
            break # kill for loop

    # to make sure we turn off the LED and close our serial connection
    print('CLOSING...')
    a.digital_write(PIN10,0) # turn LED off 
    a.close()