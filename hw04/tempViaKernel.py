#!/usr/bin/env python3
#Author: Jack Aldworth
#Date: 1/7/2024
#Description: A program that reads a TEMP101 sensor using the kernel

import time

PATH = '/sys/class/i2c-adapter/i2c-2/2-004a/hwmon/hwmon0/temp1_input'

f = open(PATH,'r')
f.seek(0)

while True:
    f.seek(0)
    print(f.read()[:-1])
    time.sleep(0.1)

