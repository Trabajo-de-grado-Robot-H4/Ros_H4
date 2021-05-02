
import smbus
import time
import struct
import RPi.GPIO as GPIO

# objeto clase smbus para i2c
bus = smbus.SMBus(1)
# Direccion del i2c arduino esclavo
address = 0x04


def readLong():
   time.sleep(0.001)
   block = bus.read_i2c_block_data(address, 0,10)
   number=""
   for i in range(10):
      number=number+chr(block[i])
   time.sleep(0.001)
   return number#struct.unpack('f', block)[0]


while True:

    number = readLong()
    print(number)
    #time.sleep(0.1)
