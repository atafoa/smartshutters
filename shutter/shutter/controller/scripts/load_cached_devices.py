import json
import os


def load_cached_devices():
	d = {}
	thing = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/known_devices.json",'r+')
	t = thing.read()
	temp = json.loads(t)
	thing.close()
	#name = temp['name']
	#mac = temp['mac_address']
	i =0
	print(temp)
	#print(type(temp))
	
	while i < len(temp):
		d['name'] = temp[0]
		d['mac_address'] = temp[1]
		i+=1
	 
	return d
d = load_cached_devices()
print (d)


