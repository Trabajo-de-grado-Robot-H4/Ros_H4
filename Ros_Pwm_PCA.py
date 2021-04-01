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


val=int(input("Inserte pwm en el canal 0: "))

if(val>=0):
  pca.channels[0].duty_cycle = val
  pca.channels[1].duty_cycle = 0
  pca.channels[2].duty_cycle = 60000
if(val<=0):
  pca.channels[0].duty_cycle = abs(val)
  pca.channels[1].duty_cycle = 60000
  pca.channels[2].duty_cycle = 0
