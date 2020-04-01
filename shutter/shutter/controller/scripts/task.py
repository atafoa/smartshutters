import sys
import bluepy.btle as btle

mac_address = sys.argv[1]
position = sys.argv[2]

class MyDelegate(btle.DefaultDelegate):
    
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        
    def handleNotification(self,cHandle,data):
		print(data)
        
device = btle.Peripheral()
device.setDelegate(MyDelegate())
#device.connect("30:AE:A4:25:14:56")
mac = str(mac_address)
device.connect(sys.argv[1])
services = device.getServices()
#print("Services discovered: ")
print(services)
characteristics = device.getCharacteristics()
# for some reason characteristics[4] sends the write to the bluetooth module. Investigate later.
#print("Characteristics discovered:")
'''
for characteristics_single in characteristics:
    print("UUID: " + str(characteristics_single.uuid))
#print("UUID for writing characteristic is:" + str(characteristics[4].uuid))
'''
characteristics[4].write(bytes(sys.argv[2]))

"""
while True:
    if device.waitForNotifications(1.0):
        print("Notification")
        continue
"""
#print("Waiting")
device.disconnect()



