#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
import RPi.GPIO as GPIO
import time
import threading

"""Pines usados """
MotorIN1 = 15
MotorIN2 = 14
MotorE1 = 18
""" Declaracion de variables """
Esfuerzo =0
Last_esfuerzo=0


def setup():

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    """ Setup del motor """
    GPIO.setup(MotorIN1,GPIO.OUT)
    GPIO.setup(MotorIN2,GPIO.OUT)
    GPIO.setup(MotorE1,GPIO.OUT)


"""inicio del programa """
def callback(data):
    global Esfuerzo
    Esfuerzo = data.position.x
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', Esfuerzo)
        
def pwm():
    global Esfuerzo
    rate = rospy.Rate(Esfuerzo) # ROS Rate at 5Hz
    GPIO.output(MotorIN1,GPIO.HIGH)  # Establecemos el sentido de giro con los pines IN1 e IN2
    GPIO.output(MotorIN2,GPIO.LOW)
    
    while not rospy.is_shutdown():
        GPIO.output(MotorE1,GPIO.HIGH)
        rate.sleep()
        
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
    global Esfuerzo 

    # spin() simply keeps python from exiting until this node is stopped
    worker = threading.Thread(target=pwm)
    worker.start()
    rospy.spin()


if __name__ == '__main__':
    setup()
    try:
            listener()
            
    except rospy.ROSInterruptException:
            destroy()
            pass
