#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point

def callback(data):
    variable_x = data.x
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', variable_x)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
#esto es una prueba
#oytaa

    rospy.Subscriber("Encoder1", Point, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
