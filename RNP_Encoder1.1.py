#!/usr/bin/env python
# license removed for brevity
""" importar librerias necesarias """
import rospy
from geometry_msgs.msg import Point # importamos el tipo de dato pose
import RPi.GPIO as GPIO # libreria para comunicacion de puestos GPIO de la raspberry
import time             # libreria para obtener el tiempo

Enc=Point() # Tipo de dato point
""" pines usados en la rapsberry"""
RoAPin = 21
RoBPin = 20
""" variables """
gain=360/(11*34*4)
grados=0
QEM=[0,-1,0,1,1,0,-1,0,0,1,0,-1,-1,0,1,0]
index=0
count=0
statep=0
""" funcion setup """
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RoAPin, GPIO.IN) # input mode
    GPIO.setup(RoBPin, GPIO.IN)

""" funcion que lee el encoder """
def rotaryDeal():

 global QEM
 global index
 global gain
 global grados
 global count
 global statep

 A= GPIO.input(RoAPin)
 B= GPIO.input(RoBPin)
 if (A==1) and (B==1):
    state=0
 if (A==1) and (B==0):
    state=1
 if (A==0) and (B==0):
    state=2
 if (A==0) and (B==1):
    state=3
 index=4*state + statep
 if (count >= 1496) or (count<=-1496):
        count=0
 count=count + QEM[index]
 statep=state

 grados=count*gain
 return (grados)
""" funcion que limpia los puertos utilizados """
def destroy():
        GPIO.cleanup()
""" funcion que publica los datos del encoder """
def talker():
    pub = rospy.Publisher('Encoder1', Point, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():


        sensor=rotaryDeal()
        Enc.x=sensor
        #Enc.position.y=3
        #Enc.position.z=12
        #rospy.loginfo(Enc)
        pub.publish(Enc)
        rate.sleep()

if __name__ == '__main__':
    setup()
    try:
        talker()
    except rospy.ROSInterruptException:
        destroy()
        pass
