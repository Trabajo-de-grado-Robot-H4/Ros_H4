""" importar librerias necesarias """
import rospy
from geometry_msgs.msg import Point # importamos el tipo de dato pose
import RPi.GPIO as GPIO # libreria para comunicacion de puestos GPIO de la raspberry
import time             # libreria para obtener el tiempo

Enc=Point() # Tipo de dato pose

def Input_data():
  Datos_pid=float(input("Inserte velocidad del motor 0 a 100: "))
  print(Datos_pid)
  return(Datos_pid)

def talker():
    pub = rospy.Publisher('Datosmotor', Point, queue_size=10)
    rospy.init_node('talkerM', anonymous=True)
    rate = rospy.Rate(1000) # 10hz
    while not rospy.is_shutdown():


        Vel=Input_data()
        Enc.x=Vel
        #Enc.position.y=3
        #Enc.position.z=12
        #rospy.loginfo(Enc)
        pub.publish(Enc)
        rate.sleep()

if __name__ == '__main__':

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
