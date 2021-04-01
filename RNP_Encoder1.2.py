#!/usr/bin/env python
# license removed for brevity

""" LIBRERÍAS """

import rospy
from geometry_msgs.msg import Point # importamos el tipo de dato pose
import RPi.GPIO as GPIO # libreria para comunicacion de puestos GPIO de la raspberry
import time             # libreria para obtener el tiempo

""" OBJETOS """

Enc=Point() # Tipo de dato point
rospy.init_node('talker1', anonymous=True)

""" PINES ENCODER """

RoAPin = 21
RoBPin = 20

""" VARIABLES """

gain=360/(11*34)
grados=0
QEM=[0,-1,0,1,1,0,-1,0,0,1,0,-1,-1,0,1,0]
index=0
count=0
statep=0

""" SETUP """

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RoAPin, GPIO.IN) # input mode
    GPIO.setup(RoBPin, GPIO.IN)
    GPIO.add_event_detect(RoAPin, GPIO.BOTH, callback=callbackEncoder)

""" INTERRUPCIÓN ENCODERS """

def callbackEncoder(RoAPin):
     global gain
     global grados
     global count

     B= GPIO.input(RoBPin)
     if (B==1):
        count=count+1
     if (B==0):
        count=count-1
     grados=count*gain
    
""" LIMPIEZA PINES """        

def destroy():
        GPIO.cleanup()
        
""" PUBLICADOR """

def talker():
    pub = rospy.Publisher('Encoder1', Point, queue_size=10)
    rate = rospy.Rate(1000)                                     # 50hz
    while not rospy.is_shutdown():
        sensor=grados
        Enc.x=sensor
        pub.publish(Enc)
        rate.sleep()
        
""" PRINCIPAL """

if __name__ == '__main__':
    setup()
    try:
        talker()
    except rospy.ROSInterruptException:
        destroy()
        pass
