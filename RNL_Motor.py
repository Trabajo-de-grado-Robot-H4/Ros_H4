#!/usr/bin/env python
import board
import busio
import adafruit_pca9685
import rospy
from geometry_msgs.msg import Pose

i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
    #asignamos la frecuencia del PWM
pca.frequency = 60

    #inicializacion de protocoño de comunicacion I2C


def callback(data):
    variable_x = data.position.x
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', variable_x)
    if abs(variable_x)<=8000:
    pca.channels[1].duty_cycle = 0
    pca.channels[2].duty_cycle = 0
    if variable_x>8000:
    pca.channels[0].duty_cycle =abs(int(variable_x))
    pca.channels[1].duty_cycle = 0
    pca.channels[2].duty_cycle = 60000

    if variable_x < -8000:
    pca.channels[0].duty_cycle =abs(int(variable_x))
    pca.channels[1].duty_cycle = 60000
    pca.channels[2].duty_cycle = 0

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
#esto es una prueba
#oytaa

    rospy.Subscriber("Datosmotor", Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        destroy()
        pass
