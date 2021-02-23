#!/usr/bin/env python
import board
import busio
import adafruit_pca968




def setup():
    #inicializacion de protocoño de comunicacion I2C
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = adafruit_pca9685.PCA9685(i2c)
    #asignamos la frecuencia del PWM
    pca.frequency = 60
    #iniciamos el canal a usar
    Canal0 = pca.channels[0]

#enviamos el PWM al Pin deseado, con
def loop():
    Canal0.duty_cycle = 0x7FFF

def Input_data():
    PWM=float(input("Inserte PWM"))

    print(PWM)
    return(PWM)


if __name__ == '__main__':     # Program start from here
        setup()
        try:
               loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program d>
