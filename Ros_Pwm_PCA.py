#!/usr/bin/env python
import board
import busio
import adafruit_pca9685

#inicializacion de protocoño de comunicacion I2C
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

#asignamos la frecuencia del PWM
pca.frequency = 60


#enviamos el PWM al Pin deseado, con

Datos_pid=[]
for v in range(4):
    val=int(input("Inserte pwm en los canales 1,2,3,4 en este orden: "))
    Datos_pid.append(val)

pca.channels[0].duty_cycle = Datos_pid[0]
pca.channels[1].duty_cycle = Datos_pid[1]
pca.channels[2].duty_cycle = Datos_pid[2]
pca.channels[3].duty_cycle = Datos_pid[3]
