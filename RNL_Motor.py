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
       self.return_value = data.position.x
     else:
       rospy.loginfo(data.position.x)


if __name__ == '__main__':
  rospy.init_node('listener')
  list = Listener()

  while list.flag:
    rospy.sleep(1)

  print('Value was non-stop')
