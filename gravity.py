#!/usr/bin/python
# A pound sign (hash) # is used as a comment so that Python ignores it
# The top line tells the computer what language we are using #!/usr/bin/python

#####YOU NEED TO EDIT THIS VALUE###############################################
height = 0.72  # height in metres of the electromagnet above the tin foil switch

#######YOU DON'T NEED TO EDIT ANYTHING BELOW HERE (but you can, it's fun!)#####
############################IGNORE THESE BITS##################################
##### We tell it what external libraries we will be using.
# In our case, we are using the PiFace###########
import pifacecommon       # Read the pifacecommon library
import pifacedigitalio    # Read the pifacedigitalio library
pifacedigitalio.init()    # Initialise the PiFace making it ready for use
pifacedigital = pifacedigitalio.PiFaceDigital() 
                          # PiFace now accessed from the pifacedigital variable
################################################ End of PiFace additions
# We are going to need to use the time library
import time
#################################################End of imported libraries#####

# Check tinfoil switch is not already pressed and exit if it is
if ( pifacedigital.input_pins[0].value == 1 ):
    print ("Warning. Tin Foil switch is pressed")
    print ("Exiting.")
    exit()
################################################################

####################COIL ENERGISING#############################
input = "n" # We don't want the countdown to start just yet
                    # so we set a variable start_the_program to n
print "Energising the coils."
# Prompt the user to hit y to start the countdown
while (input != "y"): # While input not equal to y
    input = raw_input("Press y and hit return to Energise the coil.\n")
pifacedigital.relays[0].turn_on()
print ("Coil energised.")
print ("Attach one (or more) ball bearings now.")
################################################################


#################### COUNTDOWN #################################
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
################################################################

################## DROP THE BALL ###############################
# Switch off the relay and drop the ball bearing
pifacedigital.relays[0].turn_off()

# So we need to measure the time now
start_time = time.time()

while (pifacedigital.input_pins[0].value == 0): # While switch 0 is not closed
    time.sleep(0.0001) # sleep for 10,000th of a second

#Ball has landed at this point
# Measure the time that switch 0 closed
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
#  %2.6f is a non-integer number with 2 figures before, 6 after decimal point
print("Elapsed time was %2.6f seconds" % (elapsed_time))

# Switch off relay to preserve battery power for next time
pifacedigital.relays[0].turn_off()


######## MATHS BIT ############################################################
# Distance travelled (height) = initial velocity * time + 0.5 (acceleration * time squared)
# s = ut + 0.5*g*(t ^ 2)
# s = 0 + 0.5 gt^2
# gt^2 = 2s
# g = 2s / t^2
# Acceleration due to gravity = ( 2 * height ) / (time * time)
acceleration_due_to_gravity = ( 2.0 * height ) / ((elapsed_time)**2)
print ("I calculate the acceleration due to gravity to be %1.3f (ms^-2)\n" % acceleration_due_to_gravity)


# Things to think about:
# 0: Should we repeat the experiment and take the mean of our readings?
# 1: Does the ball bearing release at the same time as the relay switches off?
# 2: Does the tin-foil slow down the ball bearing before the switch closes?
# 3: Does the Pi read fast enough? 
# 4: Air resistance?
# 5: Would it be different if we were dropping a tennis ball?
# 6: Would it be different on the Moon?
# 7: A better way to measure acceleration due to gravity?
