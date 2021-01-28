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
    Esfuerzo = data.position.x
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', Esfuerzo)
    
    p = GPIO.PWM(MotorE1, 100)  # Creamos la instancia PWM con el GPIO a utilizar y la frecuencia de la señal PWM
    p.start(0)  #Inicializamos el objeto PWM
    
    if Esfuerzo > 0:
        GPIO.output(MotorIN1,GPIO.HIGH)  # Establecemos el sentido de giro con los pines IN1 e IN2
        GPIO.output(MotorIN2,GPIO.LOW)   # Establecemos el sentido de giro con los pines IN1 e IN2
        p.ChangeDutyCycle(Esfuerzo)

    else:
        GPIO.output(MotorIN1,GPIO.LOW)   # Establecemos el sentido de giro con los pines IN1 e IN2
        GPIO.output(MotorIN2,GPIO.HIGH)  # Establecemos el sentido de giro con los pines IN1 e IN2
        p.ChangeDutyCycle(abs(Esfuerzo))
      


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
    worker = threading.Thread(name='pwm1',target=pwm,daemon=True)
    worker.start()
    rospy.spin()


def pwm():

    p = GPIO.PWM(MotorE1, 100)  # Creamos la instancia PWM con el GPIO a utilizar y la frecuencia de la señal PWM
    p.start(0)  #Inicializamos el objeto PWM

    while True:
        global Esfuerzo
       
            p.ChangeDutyCycle(Esfuerzo)


if __name__ == '__main__':
    setup()
    try:
            listener()
            
    except rospy.ROSInterruptException:
            destroy()
            pass
