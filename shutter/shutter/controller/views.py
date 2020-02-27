from django.shortcuts import render
from django.http import HttpResponse

import json
import os
import csv


def load_cached_devices():
	thing={}
	fp = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", "r")
	csvr = csv.DictReader(fp)
	for row in csvr:
		thing[row['name']]= row['mac']
	print(thing)
	return thing

known_devices = load_cached_devices()

def add_to_file():
    csv_fp = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", mode='w').close()
    csv_fp = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", mode='w')
    feilds = ['name','mac']
    writer = csv.DictWriter(csv_fp,fieldnames=feilds)
    writer.writeheader()
    for name, mac_address in known_devices.items():
    	print(name,mac_address)
    	writer.writerow({'name':name,'mac':mac_address})


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
	L = []
	d = {}
	i =0
	for name, mac_address in known_devices.items():
		d['name'] = name
		d['mac_address'] = mac_address
		L.append(dict(d))
		print(L)
		print("\n")

	t = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv","r+")
	tt = t.read()
	response = HttpResponse(json.dumps(L))
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
	print(type(known_devices))
	print(known_devices)
	temp = "added {} with mac of {}"
	
	return HttpResponse(temp.format(name,mac_address))



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







