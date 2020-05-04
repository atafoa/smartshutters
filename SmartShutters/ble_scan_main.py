# bluetooth low energy scan
# Uses Bluez for Linux
#
# sudo apt-get install bluez python-bluez
# https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=193923#p1232385
# https://www.raspberrypi.org/forums/viewtopic.php?t=197152
#26
#25
#33
#32
#
# target MAC Address: 30:AE:A4:25:14:56
# Need to use gattool BLE to connect
# sudo gatttool -b 30:AE:A4:25:14:56 -I
# char-write-req 0x002a RED

import bluepy.btle as btle
import sys
temp = []
class MyDelegate(btle.DefaultDelegate):
    
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        
    def handleNotification(self,cHandle,data):
        temp.append(data)
        print(data)

device = btle.Peripheral()
device.setDelegate(MyDelegate())
try:
    device.connect("30:AE:A4:25:14:56")
except:
    print("could not connenct")
    exit()

services = device.getServices()
print("Services discovered: ")
print(services)
characteristics = device.getCharacteristics()
# for some reason characteristics[4] sends the write to the bluetooth module. Investigate later.
print("Characteristics discovered:")
for characteristics_single in characteristics:
    print("UUID: " + str(characteristics_single.uuid))
print("UUID for writing characteristic is:" + str(characteristics[5].uuid))
characteristics[5].write(bytes("Battery\r\n"))
i = 0
while True:
    try:
        
        if device.waitForNotifications(1.0):
            print("Notification")
            continue
        if i == 10:
            break
        i=i+1
    except:
        break

print(temp[2],temp[3].strip)
oof = temp[3].strip()
print(oof)
characteristics[5].write(bytes("Sleep\r\n"))
#device.disconnect()
