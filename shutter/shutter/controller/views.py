from django.shortcuts import render
from django.http import HttpResponse

import json
import os


def load_cached_devices():
	d = {}
	thing = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/known_devices.json",'r+')
	print(type(thing.read()))
	print(thing.read())
	#oof = json.dumps(thing.readlines())
	temp = json.loads(thing.read())
	thing.close()
	i =0
'''	while i < len(temp):
		d['name'] = temp['name']
		d['mac_address'] = temp['mac_address']
		i+=1
'''
	#return d
	return d

known_devices = load_cached_devices()

def add_to_file():
    f = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/known_devices.json",'w+')
    thing = {}
    d = {}
    for name, mac_address in known_devices.items():
	    d['name'] = name
	    d['mac_address'] = mac_address
    f.write(json.dumps(d))
    f.close()    


#need to add a function that checks the devices position and loads to a dicitionary
def get_position(name):
    d = {}
    return d
    


# this returns the position of the shutter
def position(request, name):
	response = HttpResponse(name)
	return response



# this function takes in the name and position then sends an os command to the ble_scan.py file with the mac address and desired position for the motor
def move(request, name, position):
	response = HttpResponse(name + ': ' + str(position))
	return response



#this returns the list of known devices on the system
def devices(request):
	d = {}
	i = 0
	#print(known_devices)
	while i < len(known_devices):
		d['name'] = known_devices['name']
		d['mac_address'] = known_devices['mac_address']
		i+=1
	print(json.dumps(d))
	response = HttpResponse(json.dumps(d))
	#load_cached_devices()
	#print(response)
	return response



# this function scans all available devices on the network
def scan(request):
	os.system("python /home/pi/hub-repository/shutter/shutter/controller/scripts/scan_devices.py")
	f = open('/home/pi/hub-repository/shutter/shutter/controller/scripts/scan_results.json', 'r')
	scanned_devices = json.loads(f.read())
	
	response = HttpResponse(scanned_devices)
	return response
	
	
	
# this function adds devices to our list
def add_device(request, name, mac_address):
	known_devices[name] = mac_address
	response = HttpResponse()
	add_to_file()
	return response



# this functions takes out devices that are in the our list
def remove_device(request, name):
	known_devices.pop(name)
	response = HttpResponse()
	add_to_file()
	return response


#this function renames devices
def rename_device(request, old_name, new_name):
	known_devices[new_name] = known_devices[old_name]
	known_devices.pop(old_name)
	add_to_file()
	response = HttpResponse()
	return response







