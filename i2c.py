
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
   print(number)
   for i in range(20):
      number=number+chr(block[i])
      print(number)
   #return number# struct.unpack('<l', number.encode('utf-8'))[0]
   #return struct.unpack('f', number)
   #for i in range(20):
   #   number += chr(bus.read_block_data(address,1))
   #return struct.unpack('<f',bytes(block[:20]))[0]#struct.unpack('l', number)


'''
def readLong():
   block = bus.read_i2c_block_data(address, 1) #second arg is 'cmd'. It is andatory but not used in this case. It may be used by the higher level protocol
   n=struct.unpack('<l',bytes(block[:4]))[0]
   return n
'''


while True:

    number = readLong()
    print("[Arduino]", number, "mm")
    time.sleep(1)
