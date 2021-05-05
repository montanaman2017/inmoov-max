##############################################################
# MyRobotLab configuration file
# This file is generated from a running instance of MyRobotLab.
# It is meant to get MyRobotLab as close to that instance's state a possible.
# This file can be generated at any time using Runtime.save(filename)
# More information @ http://myrobotlab.org and https://github.com/myrobotlab
# version 1.1
# Updated 4/21/21 
## imports ####

from random import seed
from random import randint
import time

##############################
## Let's seed the random number generator
## which we will use down the road for random actions
##############################

seed(1)

###############################
## We start by attaching our parts to the services
##
##############################
print("=====================================")
print("Attaching parts to services")
print("=====================================")

runtime = Runtime.getInstance()
#rpi = Runtime.start('rpi', 'RasPi')
rpi = Runtime.createAndStart('rpi', 'RasPi')

# Setup the Adafruit 16 Channel I2C Servo driver 
#This is based on the PCA9685 I2C
# First we create the service and set its name to servoboard.
# and attaching it to the Adafruit16ServoDriver service
#then we attach the servoboard service to the service RasPi using
#I2C bus "1" at I2C Address "0x40" which is a Hex Address.
#servoboard = Runtime.start('servoboard', 'Adafruit16CServoDriver')
servoboard = Runtime.createAndStart('servoboard', 'Adafruit16CServoDriver')
servoboard.attach('rpi','1','0x40')
EYESUD = Runtime.createAndStart('EYESUD', 'Servo')
HEADLR = Runtime.createAndStart('HEADLR', 'Servo')
python = Runtime.start('python', 'Python')
HEADUD = Runtime.createAndStart('HEADUD', 'Servo')
EYESLR = Runtime.createAndStart('EYESLR', 'Servo')
JAW = Runtime.createAndStart('JAW', 'Servo')


##############################################################
##   #### Attach servo related items to correct
##   ###          servoboard pins
##############################################################
print("=====================================")
print("Attaching servos to servoboard pins")
print("=====================================")

EYESUD.attach(servoboard,1)
HEADLR.attach(servoboard,3)
HEADUD.attach(servoboard,4)
EYESLR.attach(servoboard,0)
JAW.attach(servoboard,2)

##############################################################
## creating client connections connections ####

##############################################################
## configuring services ####
# Servo Config : EYESUD
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
EYESUD.setRest(90)
EYESUD.map(75.0,150.0,75.0,150.0)
EYESUD.setInverted(False)
EYESUD.setVelocity(60)
EYESUD.setRest(90.0)
EYESUD.setAutoDisable(True)

# Servo Config : HEADLR
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
HEADLR.setRest(85)
HEADLR.map(30.0,145.0,30.0,145.0)
HEADLR.setInverted(False)
HEADLR.setVelocity(60)
HEADLR.setRest(85)
HEADLR.setAutoDisable(True)

# Servo Config : HEADUD
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
HEADUD.setRest(90)
HEADUD.map(0.0,180.0,0.0,180.0)
HEADUD.setInverted(False)
HEADUD.setVelocity(60)
HEADUD.setRest(90.0)
HEADUD.setAutoDisable(True)

# Servo Config : EYESLR
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
EYESLR.setRest(90)
EYESLR.map(30.0,140.0,30.0,140.0)
EYESLR.setInverted(False)
EYESLR.setVelocity(60)
EYESLR.setRest(90.0)
EYESLR.setAutoDisable(True)

# Servo Config : JAW
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
JAW.setRest(52)
JAW.map(52.0,90.0,52.0,90.0)
JAW.setInverted(False)
JAW.setVelocity(60)
JAW.setRest(52.0)
JAW.setAutoDisable(True)

def lookRight():
	EYESLR.moveTo(120)
def lookLeft():
	EYESLR.moveTo(60)
def lookForward():
	EYESLR.rest()
def lookUp():
	EYESUD.moveTo(60)
def lookDown():
	EYESUD.moveTo(140)
def headLeft():
	HEADLR.moveTo(30)
def headRight():
	HEADLR.moveTo(145)
def headForward():
	HEADLR.moveTo(85)
def jawopen():
    JAW.moveTo(90)
def jawclose():
    JAW.moveTo(52)

print("time.sleeping 5 seconds before we start")
time.sleep(5)
print("Looking right")
lookRight()
time.sleep(2)
print("Looking left")
lookLeft()
time.sleep(2)
print("Resetting eyes to middle")
lookForward()
time.sleep(2)
print("looking up")
lookUp()
time.sleep(2)
print("looking down")
lookDown()
time.sleep(2)
print("looking straight forward")
lookForward()
time.sleep(2)
#print("turning head right from my point of view")
#headRight()
#time.sleep(7)
#print("turning head left from my point of view")
#headLeft()
#time.sleep(7)
#print("turning head back to the middle")
#headForward()
#time.sleep(7)
print("opening jaw")
jawopen()
time.sleep(5)
print("closing jaw")
jawclose()
print("+++++++++++++++++++++")
print("All tests completed")
print("+++++++++++++++++++++")

print("Ain't I just amazing!!!")
