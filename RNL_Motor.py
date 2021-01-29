#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
import RPi.GPIO as GPIO
import time
import threading

class Listener(object):
   def __init__(self):
     self.flag = True
     self.sub = rospy.Subscriber('Datosmotor', Pose, self.echo)


   def echo(self, data):  # data.msg can be 'stop' string or any other string
     if data.position.x == 0:
       self.flag = False
     else:
       rospy.loginfo(data.position.x)
       self.return_value = data.position.x
def pwm():
    while True:
            rospy.init_node('listener')
            list = Listener()
            print(list.return_value)



if __name__ == '__main__':
    try:
        pwm()
    except rospy.ROSInterruptException:
        pass
