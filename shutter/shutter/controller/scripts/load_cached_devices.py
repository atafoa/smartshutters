import json
import os


def load_cached_devices():
	d = {}
	t = {}
	thing = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/known_devices.json",'r+')
	temp = json.loads(thing.read())
	print(temp)
	#x = temp.values()
	#print(x)
	thing.close()
	print(type(temp))
	name = temp['name']
	mac = temp['mac_address']
	print(name,mac)
	
	print(len(temp))
	
	return d
d = load_cached_devices()


