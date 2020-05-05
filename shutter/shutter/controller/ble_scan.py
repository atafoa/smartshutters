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
import time

class MyDelegate(btle.DefaultDelegate):
    
    device = btle.Peripheral()
    list_to_return = []
    
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        
    def handleNotification(self,cHandle,data):
        self.list_to_return.append(data)
        
    def connect(self,mac_address):
        self.device.connect(mac_address)
        self.device.setDelegate(MyDelegate())
    
    def discover_services_and_characteristics(self):
        services = self.device.getServices()
        print("Services discovered: ")
        print(services)
        characteristics = self.device.getCharacteristics()
        # for some reason characteristics[5] sends the write to the bluetooth module. Investigate later.
        print("Characteristics discovered:")
        for characteristics_single in characteristics:
            print("UUID: " + str(characteristics_single.uuid))
        print("UUID for writing characteristic is:" + str(characteristics[4].uuid))
        return characteristics,services
    def send_command(self,position):
        characteristics,services = self.discover_services_and_characteristics()
        characteristics[5].write(bytes(position,"utf-8"))
    
    def check_notifications(self):
        if self.device.waitForNotifications(1.0):
            print("Notification")
            try:
                while self.device.waitForNotifications(1.0):
                    print("note note")
                    continue
            finally:
                return self.list_to_return
    
    def disconnect(self):
        print("Disconnecting ...")
        self.device.disconnect()
        print("Disconnected")
        
"""
while True:
    if device.waitForNotifications(1.0):
        print("Notification")
        continue
"""
