### Author: Jack Aldworth
### Date: 1/18/2024
# LEDUpDown
A kernal program that turns off and LED while a button is pressed but otherwise leaves it on
### Pins
P8_12 : LED    P8_11 : Button
### Setup
Use command sudo insmod LEDUpDown.ko to start and sudo rmmod LEDUpDown to stop
# 2LED2Buttons
A kernal program that toggles the states of 2 LEDs
### Pins
P8_12 , P8_14 : LEDs | P8_11 , P8_17 : Buttons
### Setup
Use command sudo insmod 2LED2Buttons.ko to start and sudo rmmod 2LED2Buttons to stop
# Etch-A-SketchViaKernal
A program that allows for a 8x8 Matrix Etch-a-sketch to have tilt controls
### Pins
P9_19, P9_20 : i2c connection
### Setup
Just run the program
