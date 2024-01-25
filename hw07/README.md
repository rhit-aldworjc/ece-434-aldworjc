### Author: Jack Aldworth
### Date: 1/25/2024
# BB-W1-P9.14-00A0
A device tree that allows for 1-wire temperature sensors to be controled by pin P9_14
### Setup
Wire pin P9_14 to the signal pin on the sensors. copy both files to /lib/firmware. Add the line uboot_overlay_addr4=BB-W1-P9.14-00A0.dtbo to /boot/uEnv.txt.
# Flask service
Automatically opens flask server from hw04 when board is turned on.
### Setup
while in folder type command: sudo systemctl enable flask. Then sudo reboot.
