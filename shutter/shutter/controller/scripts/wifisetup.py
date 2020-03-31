




'''

from bluetool import Bluetooth
import signal
bluetooth = Bluetooth()
bluetooth.scan()
devices = bluetooth.get_available_devices()
print(devices)
print(bluetooth.trust("EC:AA:25:34:60:36"))
print("\n\n\n\n")
#print(bluetooth.get_devices_to_pair())

print(bluetooth.connect("EC:AA:25:34:60:36"))

print(bluetooth.disconnect("EC:AA:25:34:60:36"))
'''
'''
from wifi import Scheme,Cell

target_ssid = 'Cell(ssid=NETGEAR33)'
target_pwd = "bluepiano174"

def wifiscan():
	Cell.all('wlan0')
	allSSID = list(Cell.all("wlan0"))[0]
	myssid = Scheme.for_cell('wlan0','home',allSSID,target_pwd)
	myssid.activate()
	
	myssid = Scheme.find('wlan0','home')
	myssid.activate()
	
	
	
wifiscan()
		
	
'''
