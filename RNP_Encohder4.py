#!/usr/bin/env python
# license removed for brevity
""" importar librerias necesarias """
import rospy
from geometry_msgs.msg import Pose # importamos el tipo de dato pose
import RPi.GPIO as GPIO # libreria para comunicacion de puestos GPIO de la raspberry
import time             # libreria para obtener el tiempo

Enc=Pose() # Tipo de dato pose
""" pines usados en la rapsberry"""
RoAPin1 = 20    
RoBPin1 = 21 
""" """
RoAPin2 = 12    
RoBPin2 = 16 
""" """
RoAPin3 = 19    
RoBPin3 = 26 
""" """
RoAPin3 = 6   
RoBPin3 = 13 
""" variables """
globalCounter = 0.0
gain=0.97593582887
flag = 0
Last_RoB_Status = 0.0
Current_RoB_Status = 0.0
grados=0.0

""" funcion setup """
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RoAPin1, GPIO.IN) # input mode
    GPIO.setup(RoBPin1, GPIO.IN)
    """ """
    GPIO.setup(RoAPin2, GPIO.IN) # input mode
    GPIO.setup(RoBPin2, GPIO.IN)
    """ """
    GPIO.setup(RoAPin3, GPIO.IN) # input mode
    GPIO.setup(RoBPin3, GPIO.IN)
    
    """ """
    GPIO.setup(RoAPin4, GPIO.IN) # input mode
    GPIO.setup(RoBPin4, GPIO.IN)
""" funcion que lee el encoder """
def rotaryDeal():
 global flag
 global Last_RoB_Status
 global Current_RoB_Status
 global globalCounter
 global gain
 global grados

 Last_RoB_Status = GPIO.input(RoBPin)
 while((not GPIO.input(RoAPin1)) and (not GPIO.input(RoAPin2)) and (not GPIO.input(RoAPin3)) and (not GPIO.input(RoAPin4))  ):
   Current_RoB_Status = GPIO.input(RoBPin)
   flag = 1
 
 if flag == 1:
      flag = 0
      if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
         globalCounter = globalCounter + 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
      if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
         globalCounter = globalCounter - 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
 grados=globalCounter*gain
 return (grados)
""" funcion que limpia los purtos utilizados """
def destroy():
        GPIO.cleanup()
""" funcion que publica los datos del encoder """
def talker():
    pub = rospy.Publisher('Encoder', Pose, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        
        sensor=rotaryDeal()
        Enc.position.x=sensor
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
