
import json
import os


def load_cached_devices():
	d = {}
	t = {}
	thing = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/known_devices.json",'r+')
	temp = json.loads(thing.read())
	print(temp)
	#x = temp.values()
	#print(x)
	thing.close()
	for x in temp.items:
            print(x.keys)
	return d
