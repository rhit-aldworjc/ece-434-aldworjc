### Author: Jack Aldworth
### Date: 1/11/2024
# mmapButtonLEDs
A simple gpio program using mmap
### Pins
LED1 = P8_12 LED2 = P9_14 BUTTON1 = P9_11 BUTTON2 = P9_17
### Setup
run with permissions (sudo)
# mmapQuickToggle
Test to see how fast a gpio pin can be flipped using mmap
### Pins
P8_12
### Setup
run with permissions (sudo
### notes
I got a speed of aproximitly 4.43MHz
# tempViaKernel
Reads and prints tempeture valuse from at TMP101 using the Kernel
### Pins
i2c pins (P9_19, P9_20)
### Setup
Just run the program
# flaskServer
Runs a webserver that controls an 8x8 LED etch-a-sketch
# Pins
i2c pins (P9_19, P9_20)
### Setup
Run program then type 192.168.7.2:8081 into a webbrowser then use the controls on the browser to control the etch-a-sketch
