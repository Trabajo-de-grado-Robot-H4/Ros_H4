
from smbus2 import SMBus
import time
import struct
import RPi.GPIO as GPIO

# objeto clase smbus para i2c
bus = SMBus(1)
# Direccion del i2c arduino esclavo
address = 0x61



def readLong():
   block = bus.read_i2c_block_data(address, 1,10)
   number=""
   for i in range(10):
     number=number+chr(block[i])
   return number


while True:

    number = readLong()
    print(number)
    #time.sleep(1)
