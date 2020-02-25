import json
import os


def load_cached_devices():
	d = {}
	thing = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/known_devices.json",'r+')
	t = thing.read()
	temp = json.dumps(t)
	thing.close()
	#name = temp['name']
	#mac = temp['mac_address']
	i =0
	#print(temp)
	#print(type(temp))
	
	while i < len(temp):
		d[0] = temp[0]
		d[1] = temp[1]
		i+=1
	 
	return d
d = load_cached_devices()
print (d)


