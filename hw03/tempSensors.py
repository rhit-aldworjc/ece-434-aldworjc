#!/usr/bin/env python3

import smbus
import time

bus = smbus.SMBus(2)
sensor1 = 0x4a
sensor2 = 0x49

while True:
    temp = bus.read_byte_data(sensor1,0)
    print("Left Sensor temp: ",temp)
    temp = bus.read_byte_data(sensor2,0)
    print("Right Sensor temp: ",temp)
    time.sleep(1)
