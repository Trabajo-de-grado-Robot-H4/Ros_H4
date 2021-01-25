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
RoAPin4 = 6   
RoBPin4 = 13 
""" variables """
globalCounter1,globalCounter2,globalCounter3,globalCounter4 = 0.0
gain=0.97593582887
flag1=0
flag2=0
flag3=0
flag4 = 0
Last_RoB_Status1=0.0
Last_RoB_Status2=0.0
Last_RoB_Status3=0.0
Last_RoB_Status4 = 0.0
Current_RoB_Status1=0.0
Current_RoB_Status2=0.0
Current_RoB_Status3=0.0
Current_RoB_Status4 = 0.0
grados1=0.0
grados2=0.0
grados3=0.0
grados4=0.0
grados=[0,0,0,0]

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
 global flag1
 global flag2
 global flag3
 global flag4
 global Last_RoB_Status1
 global Last_RoB_Status2
 global Last_RoB_Status3
 global Last_RoB_Status4 
 global Current_RoB_Status1
 global Current_RoB_Status2
 global Current_RoB_Status3
 global Current_RoB_Status4
 global globalCounter1
 global globalCounter2
 global globalCounter3
 global globalCounter4
 global grados1
 global grados2
 global grados3
 global grados4
 global gain
 global grados
 

 Last_RoB_Status1 = GPIO.input(RoBPin1)
 Last_RoB_Status2 = GPIO.input(RoBPin2)
 Last_RoB_Status3 = GPIO.input(RoBPin3)
 Last_RoB_Status4 = GPIO.input(RoBPin4)
    
 while((not GPIO.input(RoAPin1)) and (not GPIO.input(RoAPin2)) and (not GPIO.input(RoAPin3))  and (not GPIO.input(RoAPin4)) ):
   Current_RoB_Status1 = GPIO.input(RoBPin1)
   flag1 = 1
   Current_RoB_Status2 = GPIO.input(RoBPin2)
   flag2 = 1
   Current_RoB_Status3 = GPIO.input(RoBPin3)
   flag3 = 1
   Current_RoB_Status4 = GPIO.input(RoBPin4)
   flag4 = 1
 
 if flag1 == 1:
      flag1 = 0
      if (Last_RoB_Status1 == 0) and (Current_RoB_Status1 == 1):
         globalCounter1 = globalCounter1 + 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
      if (Last_RoB_Status1 == 1) and (Current_RoB_Status1 == 0):
         globalCounter1 = globalCounter1 - 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
 if flag2 == 1:
      flag2 = 0
      if (Last_RoB_Status2 == 0) and (Current_RoB_Status2 == 1):
         globalCounter2 = globalCounter2 + 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
      if (Last_RoB_Status2 == 1) and (Current_RoB_Status2 == 0):
         globalCounter2 = globalCounter2 - 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
 if flag3 == 1:
      flag3 = 0
      if (Last_RoB_Status3 == 0) and (Current_RoB_Status3 == 1):
         globalCounter3 = globalCounter3 + 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
      if (Last_RoB_Status3 == 1) and (Current_RoB_Status3 == 0):
         globalCounter3 = globalCounter3 - 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
 if flag4 == 1:
      flag4 = 0
      if (Last_RoB_Status4 == 0) and (Current_RoB_Status4 == 1):
         globalCounter4 = globalCounter4 + 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
      if (Last_RoB_Status4 == 1) and (Current_RoB_Status4 == 0):
         globalCounter4 = globalCounter4 - 1.0
         #print ('globalCounter =')
         #print ("{0:.3f}".format(globalCounter*gain))
 grados3=globalCounter3*gain
 grados1=globalCounter1*gain
 grados2=globalCounter2*gain
 grados4=globalCounter4*gain

 grados=[grados1,grados2,grados3,grados4]
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
        Enc.position.x=sensor[0]
        Enc.position.y=sensor[1]
        Enc.position.z=sensor[2]
        Enc.orientation.x=sensor[3]
        rospy.loginfo(Enc)
        pub.publish(Enc)
        rate.sleep()

if __name__ == '__main__':
    setup()
    try:
        talker()
    except rospy.ROSInterruptException:
        destroy()
        pass
