# bluetooth low energy scan
# Uses Bluez for Linux
#
# sudo apt-get install bluez python-bluez
# https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=193923#p1232385
# https://www.raspberrypi.org/forums/viewtopic.php?t=197152
#
#
#
# target MAC Address: 30:AE:A4:25:14:56
# Need to use gattool BLE to connect
# sudo gatttool -b 30:AE:A4:25:14:56 -I
# char-write-req 0x002a RED

import bluepy.btle as btle

device = btle.Peripheral()
device.connect("30:AE:A4:25:14:56")
services = device.getServices()
print("Services discovered: ")
print(services)
characteristics = device.getCharacteristics()
# for some reason characteristics[4] sends the write to the bluetooth module. Investigate later.
print("Characteristics discovered:")
for characteristics_single in characteristics:
    print("UUID: " + str(characteristics_single.uuid))
print("UUID for writing characteristic is:" + str(characteristics[4].uuid))
characteristics[4].write(bytes("PURPLE"))
device.disconnect()
