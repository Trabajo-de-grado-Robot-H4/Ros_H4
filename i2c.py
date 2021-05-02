
import smbus
import time
import struct
import RPi.GPIO as GPIO

# objeto clase smbus para i2c
bus = smbus.SMBus(1)
# Direccion del i2c arduino esclavo
address = 0x04


def readLong():
   block = bus.read_i2c_block_data(address, 0,20)
   return block#struct.unpack('f', block)[0]


while True:

    number = readLong()
    print(number)
    time.sleep(0.1)
