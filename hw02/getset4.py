#!/usr/bin/env python3
#Author: Jack Aldworth
#Date Made: 12/12/2023
#Desription: Changes LED states to match switch state

import gpiod
import sys

CONSUMER='getset'
CHIP='1'
getoffsets=[14,15,12,13]# P8_16, P8_15, P8_12, P8_11
setoffests=[18,19,28,29] # P9_14, P9_16, P9_12, P8_26

chip = gpiod.Chip(CHIP)

getlines = chip.get_lines(getoffsets)
getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_IN)

setlines = chip.get_lines(setoffests)
setlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT)

print("Hit ^C to stop")
while True:
    vals = getlines.get_values()
    #print(vals)
    # for val in vals:
    #     print(val, end=' ')
    # print('\r', end='')
    #led = [val[0]]
    setlines.set_values(vals) #change to led if unblanced array
