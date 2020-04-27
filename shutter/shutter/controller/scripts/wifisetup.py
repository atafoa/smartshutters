import sys
from wifi import Scheme,Cell

ssid = sys.argv[1]
pwd = sys.argv[2]

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
		
	
