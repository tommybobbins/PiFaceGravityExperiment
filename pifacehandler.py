#!/usr/bin/python
import pifacecommon
import pifacedigitalio
import time
pifacedigitalio.init()
pifacedigital = pifacedigitalio.PiFaceDigital()
def woo_woo(start,finish):
    for i in range(start,finish):
        pifacedigital.output_pins[i].value=1
        time.sleep(0.05)
    for i in reversed(range(start,finish)):
        pifacedigital.output_pins[i].value=0
        time.sleep(0.05)

def start_the_countdown():
    if ( pifacedigital.input_pins[0].value == 1 ):
        print ("Warning. Tin Foil switch is pressed")
        print ("I'm out of here.")
        exit()
    input = "n" # We don't want the countdown to start just yet
                        # so we set a variable start_the_program to n
    print "Energising the coils."
    # Prompt the user to hit y to start the countdown
    while (input != "y"): # While input not equal to y
        input = raw_input("Press y and hit return to Energise the coil.\n")
    pifacedigital.relays[0].turn_on()
    print ("Coil energised")
    input = "n"
    while (input != "y"): # While input not equal to y
        input = raw_input("Press y and hit return to begin the countdown.\n")
    print ("5");
    time.sleep(1);
    print ("4");
    time.sleep(1);
    print ("3");
    time.sleep(1);
    print ("2");
    time.sleep(1);
    print ("1");
    time.sleep(1);
    print ("freefall");
