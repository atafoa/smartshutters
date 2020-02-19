from bluetool import Bluetooth
import json
bluetooth = Bluetooth()
bluetooth.scan()
f = open("/home/pi/hub-repository/hello/shutter/templates/shutter/scanResult.txt","w")
devices = bluetooth.get_available_devices() #list object
d={}
print(devices)
for x in devices:
    d[x['name']] = x['mac_address']
    

#print(d)
j = json.dumps(d)
print(j)
