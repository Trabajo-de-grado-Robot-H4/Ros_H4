
import smbus
import time
import struct
import RPi.GPIO as GPIO

# objeto clase smbus para i2c
bus = smbus.SMBus(1)
# Direccion del i2c arduino esclavo
address = 0x04

def readLong():
   block = bus.read_i2c_block_data(address, 1)
   #number = bus.read_byte(address)
   number=""
   for i in range(10):
      number= number+chr(block[i])
      time.sleep(0.02)
   print(read_word_data(address))
   return number


'''
def readLong():
   block = bus.read_i2c_block_data(address, 1) #second arg is 'cmd'. It is andatory but not used in this case. It may be used by the higher level protocol
   n=struct.unpack('<l',bytes(block[:4]))[0]
   return n
'''


while True:

    number = readLong()
    print("[Arduino]", number, "mm")
    #time.sleep(0.1)
