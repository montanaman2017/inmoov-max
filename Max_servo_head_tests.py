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


eyes_up_down_pin 	= 1
head_left_right_pin = 8 # was 3
head_up_down_pin 	= 0 # was 4
eyes_left_right_pin = 3 # was 0
jaw_pin 			= 2

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

#rpi = Runtime.start('rpi', 'RasPi')
rpi = Runtime.start('rpi', 'RasPi')

# start local speech so we can say things
mouth = Runtime.start('mouth', 'LocalSpeech')
mouth.speakBlocking('Hello, I have a mouth ! I like having a mouth. I can use it to say things')

mouth.speakBlocking('I wish I had a brain - wait, making a brain')
brain = Runtime.start('brain', 'ProgramAB')
mouth.speakBlocking('I wish I had an ear - wait, making an ear')
ear = Runtime.start('ear', 'WebkitSpeechRecognition')

# Setup the Adafruit 16 Channel I2C Servo driver 
#This is based on the PCA9685 I2C
# First we create the service and set its name to servoboard.
# and attaching it to the Adafruit16ServoDriver service
#then we attach the servoboard service to the service RasPi using
#I2C bus "1" at I2C Address "0x40" which is a Hex Address.
#servoboard = Runtime.start('servoboard', 'Adafruit16CServoDriver')
mouth.speakBlocking('I am about to start a servoboard and a bunch of servos')
servoboard = Runtime.start('servoboard', 'Adafruit16CServoDriver')
servoboard.attach('rpi','1','0x40')
EYESUD = Runtime.start('EYESUD', 'Servo')
HEADLR = Runtime.start('HEADLR', 'Servo')
python = Runtime.start('python', 'Python')
HEADUD = Runtime.start('HEADUD', 'Servo')
EYESLR = Runtime.start('EYESLR', 'Servo')
JAW = Runtime.start('JAW', 'Servo')


##############################################################
##   #### Attach servo related items to correct
##   ###          servoboard pins
##############################################################
print("=====================================")
print("Attaching servos to servoboard pins")
print("=====================================")
mouth.speakBlocking('now I am attaching the servos to the servoboard')
EYESUD.attach(servoboard, eyes_up_down_pin)
HEADLR.attach(servoboard, head_left_right_pin)
HEADUD.attach(servoboard, head_up_down_pin)
EYESLR.attach(servoboard, eyes_left_right_pin)
JAW.attach(servoboard, jaw_pin)


mouth.speakBlocking('now I am configuring the servos but really this should occur before attaching')

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
	mouth.speak("I'm looking right")
	EYESLR.moveTo(120)
	HEADLR.moveTo(160)
def lookLeft():
	mouth.speak("I'm looking left")
	EYESLR.moveTo(60)
	HEADLR.moveTo(10)
def lookForward():
	mouth.speak("I'm looking forward")
	EYESLR.rest()
	HEADLR.rest()
	HEADUD.rest()
def lookUp():
	mouth.speak("I'm looking up")
	EYESUD.moveTo(60)
	HEADUD.moveTo(10)
def lookDown():
	mouth.speak("I'm looking down")
	EYESUD.moveTo(140)
	HEADUD.moveTo(140)
def headLeft():
	HEADLR.moveTo(30)
	HEADLR.moveTo(10)
def headRight():
	HEADLR.moveTo(145)
	HEADLR.moveTo(160)
def headForward():
	HEADLR.moveTo(85)
def jawopen():
    JAW.moveTo(90)
    EYESLR.rest()
    HEADLR.rest()
    HEADUD.rest()
def jawclose():
    JAW.moveTo(52)
    EYESLR.rest()
    HEADLR.rest()
    HEADUD.rest()

print("time.sleeping 5 seconds before we start")
time.sleep(5)
print("Looking right")
mouth.speakBlocking('Looking right')
lookRight()
time.sleep(2)
print("Looking left")
mouth.speakBlocking('Looking left')
lookLeft()
time.sleep(2)
print("Resetting eyes to middle")
mouth.speakBlocking('Resetting eyes to middle')
lookForward()
time.sleep(2)
print("looking up")
mouth.speakBlocking('looking up')
lookUp()
time.sleep(2)
print("looking down")
mouth.speakBlocking('looking down')
lookDown()
time.sleep(2)
print("looking straight forward")
mouth.speakBlocking('looking straight forward')
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
mouth.speakBlocking('opening jaw')
jawopen()
time.sleep(5)
print("closing jaw")
mouth.speakBlocking('closing jaw')
jawclose()
print("+++++++++++++++++++++")
print("All tests completed")
print("+++++++++++++++++++++")

print("Ain't I just amazing!!!")
mouth.speakBlocking("Aint I just amazing!")

