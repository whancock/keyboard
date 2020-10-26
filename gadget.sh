#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p usbgadget
cd usbgadget

ID_VENDOR="0x1d6b"
ID_PRODUCT="0x0104"

echo "0x0200" > bcdUSB
echo "0x02" > bDeviceClass
echo "0x00" > bDeviceSubClass
echo "0x3066" > bcdDevice
echo $ID_VENDOR > idVendor
echo $ID_PRODUCT > idProduct

# OS Descriptors
echo "1" > os_desc/use
echo "0xcd" > os_desc/b_vendor_code
echo "MSFT100" > os_desc/qw_sign

mkdir strings/0x409
echo "9112473" > strings/0x409/serialnumber
echo "Will Hancock" > strings/0x409/manufacturer
echo "SnackBox" > strings/0x409/product

# Gadgets
mkdir -p functions/rndis.usb0  # network
# mkdir -p functions/acm.usb0    # serial

mkdir -p configs/c.1
echo 250 > configs/c.1/MaxPower
ln -s functions/rndis.usb0 configs/c.1/
# ln -s functions/acm.usb0   configs/c.1/

# IStick
mkdir -p configs/c.1/strings/0x409
echo "Config 1: RNDIS network" > configs/c.1/strings/0x409/configuration

echo RNDIS   > functions/rndis.usb0/os_desc/interface.rndis/compatible_id
echo 5162001 > functions/rndis.usb0/os_desc/interface.rndis/sub_compatible_id

ln -s configs/c.1 os_desc

# Add functions here
# see gadget configurations below
# End functions
ls /sys/class/udc > UDC
