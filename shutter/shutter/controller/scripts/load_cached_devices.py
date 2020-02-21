import json
import os


def load_cached_devices():
	d = {}
	thing = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/known_devices.json",'r+')
	temp = json.loads(thing.read())
	thing.close()
	name = temp['name']
	mac = temp['mac_address']
	i =0
	while i < len(temp):
		d['name'] = temp['name']
		d['mac_address'] = temp['mac_address']
		i+=1

	return d
d = load_cached_devices()
print (d)

