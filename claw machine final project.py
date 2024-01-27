import RPi.GPIO as GPIO
import turtle

#global var
screen=turtle.Screen()

#constants
SPEED=50

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
MotorFB1={'EN':25,'input1':24,'input2':23}
MotorFB2={'EN':17,'input1':27,'input2':22}
MotorLR1={'EN':21,'input1':20,'input2':16}
MotorLR2={'EN':13,'input1':19,'input2':26}
for element in MotorFB1:
    GPIO.setup(MotorFB1[element], GPIO.OUT)
    GPIO.setup(MotorFB2[element], GPIO.OUT)
    GPIO.setup(MotorLR1[element], GPIO.OUT)
    GPIO.setup(MotorLR2[element], GPIO.OUT)

ENfb1 = GPIO.PWM(MotorFB1['EN'], 100)
ENfb2 = GPIO.PWM(MotorFB2['EN'], 100)
ENlr1 = GPIO.PWM(MotorLR1['EN'], 100)
ENlr2 = GPIO.PWM(MotorLR2['EN'], 100)
ENfb1.start(0)
ENfb2.start(0)
ENlr1.start(0)
ENlr2.start(0)

#functions
def stop_func():
    global ENfb1,ENfb2,ENlr1,ENlr2
    ENfb1.ChangeDutyCycle(0)
    ENfb2.ChangeDutyCycle(0)
    ENlr1.ChangeDutyCycle(0)
    ENlr2.ChangeDutyCycle(0)

#keybinds
def forward():
    global ENfb1,ENfb2
    ENfb1.ChangeDutyCycle(SPEED)
    ENfb2.ChangeDutyCycle(SPEED)
    GPIO.output(MotorFB1['input1'], GPIO.HIGH)
    GPIO.output(MotorFB1['input2'], GPIO.LOW)
    GPIO.output(MotorFB2['input1'], GPIO.LOW)
    GPIO.output(MotorFB2['input2'], GPIO.HIGH)
    print('forward')
def backward():
    global ENfb1,ENfb2
    ENfb1.ChangeDutyCycle(SPEED)
    ENfb2.ChangeDutyCycle(SPEED)
    GPIO.output(MotorFB1['input1'], GPIO.LOW)
    GPIO.output(MotorFB1['input2'], GPIO.HIGH)
    GPIO.output(MotorFB2['input1'], GPIO.HIGH)
    GPIO.output(MotorFB2['input2'], GPIO.LOW)
    print('backward')
def left():
    ENlr1.ChangeDutyCycle(SPEED)
    ENlr2.ChangeDutyCycle(SPEED)
    GPIO.output(MotorLR1['input1'], GPIO.HIGH)
    GPIO.output(MotorLR1['input2'], GPIO.LOW)
    GPIO.output(MotorLR2['input1'], GPIO.LOW)
    GPIO.output(MotorLR2['input2'], GPIO.HIGH)
    print('left')
def right():
    ENlr1.ChangeDutyCycle(SPEED)
    ENlr2.ChangeDutyCycle(SPEED)
    GPIO.output(MotorLR1['input1'], GPIO.LOW)
    GPIO.output(MotorLR1['input2'], GPIO.HIGH)
    GPIO.output(MotorLR2['input1'], GPIO.HIGH)
    GPIO.output(MotorLR2['input2'], GPIO.LOW)
    print('right')

def up():
    pass
def down():
    pass

screen.listen()
screen.onkey(forward,'Up')
screen.onkey(backward,'Down')
screen.onkey(left,'Left')
screen.onkey(right,'Right')

turtle.done