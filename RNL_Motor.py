#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
import RPi.GPIO as GPIO
import time
import threading
import logging
logging.basicConfig( level=logging.DEBUG,
    format='[%(levelname)s] - %(threadName)-10s : %(message)s')

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
    logging.debug('Lanzado')
    while True:
            list = Listener()
            logging.debug(list.return_value)



if __name__ == '__main__':

        rospy.init_node('listener')
        list=Listener()
        d = threading.Thread(target=pwm, name='Daemon')
        d.setDaemon(True)
        d.start()
        while list.flag:
             rospy.sleep(1)
        print('Value was non-stop')
