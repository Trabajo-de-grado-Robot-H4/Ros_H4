#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
import RPi.GPIO as GPIO
import time


"""Pines usados """
MotorIN1 = 15
MotorIN2 = 14
MotorE1 = 18
""" Declaracion de variables """
Last_esfuerzo=0
Esfuerzo=0

def setup():

    GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)

    """ Setup del motor """
    GPIO.setup(MotorIN1,GPIO.OUT)
    GPIO.setup(MotorIN2,GPIO.OUT)
    GPIO.setup(MotorE1,GPIO.OUT)


"""inicio del programa """
def callback(data):
     Esfuerzo = data.position.x
     p = GPIO.PWM(MotorE1, 100)  # Creamos la instancia PWM con el GPIO a utilizar y la frecuencia de la señal PWM
     p.start(0)  #Inicializamos el objeto PWM
     p.ChangeDutyCycle(Last_esfuerzo)
        
     if Esfuerzo > 0:
         GPIO.output(MotorIN1,GPIO.HIGH)  # Establecemos el sentido de giro con los pines IN1 e IN2
         GPIO.output(MotorIN2,GPIO.LOW)   # Establecemos el sentido de giro con los pines IN1 e IN2
         p.ChangeDutyCycle(Esfuerzo)
         rospy.loginfo(rospy.get_caller_id() + 'I heard %f', Esfuerzo)
         Last_esfuerzo=Esfuerzo
     else:
         GPIO.output(MotorIN1,GPIO.LOW)   # Establecemos el sentido de giro con los pines IN1 e IN2
         GPIO.output(MotorIN2,GPIO.HIGH)  # Establecemos el sentido de giro con los pines IN1 e IN2
         p.ChangeDutyCycle(abs(Esfuerzo))
         rospy.loginfo(rospy.get_caller_id() + 'I heard %f', Esfuerzo)
         Last_esfuerzo=Esfuerzo

def destroy():
        GPIO.cleanup()
def listener():
  
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('ListenerM', anonymous=True)

    rospy.Subscriber("Datosmotor", Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    #ese te un cambio

if __name__ == '__main__':
    setup()
    try:
            listener()
    except rospy.ROSInterruptException:
            destroy()
            pass
