#!/usr/bin/python
import sys
import time
import smbus
from time import sleep
from retry import retry

@retry()
def func1(i2c,address):
    i2c.write_i2c_block_data(address,0x00,[])

@retry()
def func2(i2c,address):
    i2c.write_i2c_block_data(address,0x03,[0x00,0x04])

@retry()
def func3(i2c,address):
    ret = i2c.read_i2c_block_data(address,0,6)
    return(ret)
   
def get_value():
    i2c = smbus.SMBus(1)
    address = 0x5c
    func1(i2c,address)
    sleep(0.003)
    func2(i2c,address)
    sleep(0.015)
    block = func3(i2c,address)
    humidity = (block[2] << 8 | block[3])/10.0
    temperature = (block[4] << 8 | block[5])/10.0
    unix_time=int(time.time())
    print("humidity\t%f\t%d" % (humidity,unix_time))

if __name__ == '__main__':
    get_value()
