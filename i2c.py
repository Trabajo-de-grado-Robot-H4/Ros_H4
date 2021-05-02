
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
   return struct.unpack('f', block)[0]
'''
def readLong():
   block = bus.read_i2c_block_data(address, 1)
   number=""
   for i in range(32):
      number= number+chr(block[i])
      print(number)
   return number
'''
while True:

    number = readLong()
    print(number)
    time.sleep(0.1)
