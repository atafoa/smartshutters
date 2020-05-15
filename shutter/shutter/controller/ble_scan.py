###@package ble_scan.py
# bluetooth low energy scan
# Uses Bluez for Linux
#
# sudo apt-get install bluez python-bluez
# https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=193923#p1232385
# https://www.raspberrypi.org/forums/viewtopic.php?t=197152
#

import bluepy.btle as btle
import time
### this class is how we can move the shutter
class MyDelegate(btle.DefaultDelegate):
    
    device = btle.Peripheral()
    list_to_return = []
    
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
    ### recieves notifications from the motor and sends it to the app    
    def handleNotification(self,cHandle,data):
        self.list_to_return.append(data)
    ### how the hub connects to the motor    
    def connect(self,mac_address):
        self.device.connect(mac_address)
        self.device.setDelegate(MyDelegate())
    ### prints out all the characteristics of the motor
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
### this function sends the commands to the motor
    def send_command(self,position):
        characteristics,services = self.discover_services_and_characteristics()
        characteristics[5].write(bytes(position,"utf-8"))
    ### checks if there are notifications from the motor
    def check_notifications(self):
        if self.device.waitForNotifications(1.0):
            print("Notification")
            try:
                while self.device.waitForNotifications(1.0):
                    print("note note")
                    continue
            finally:
                return self.list_to_return
### disconnects the class from the motor    
    def disconnect(self):
        print("Disconnecting ...")
        self.device.disconnect()
        print("Disconnected")

