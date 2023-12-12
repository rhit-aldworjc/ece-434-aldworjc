#!/usr/bin/env python3
# //////////////////////////////////////
# 	getset.py
#  Get the value of P8_16 and write it to P9_14. 
#     P8_16 is line 14 on chip 1.  P9_14 is line 18 of chip 1.
# 	Wiring:	Attach a switch to P8_16 and 3.3V and an LED to P9_14.
# 	Setup:	sudo apt uupdate; sudo apt install libgpiod-dev
#           Run: gpioinfo | grep -i -e chip -e P9_14 to find chip and line numbers
# 	See:	https://github.com/starnight/libgpiod-example/blob/master/libgpiod-led/main.c
# //////////////////////////////////////
# Based on https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/tree/bindings/python/examples

import gpiod
import sys

CONSUMER='getset'
CHIP='1'
getoffsets=[14,15,12,13]# P8_16, P8_15, P8_12, P8_11
setoffests=[18,19,28,29] # P9_14, P9_16, P8_5, P8_6

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
