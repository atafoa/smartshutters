from django.shortcuts import render
from django.http import HttpResponse

import json
import os
import time
from . import ble_scan
import csv



def load_cached_devices():
	thing={}
	fp = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", "r")
	csvr = csv.DictReader(fp)
	for row in csvr:
		thing[row['name']]= row['mac']
	print(thing)
	return thing

known_devices = load_cached_devices()

def add_to_file():
    csv_fp = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", mode='w').close()
    csv_fp = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", mode='w')
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

	#t = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv","r+")
	#tt = t.read()
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
	if check(name) == 0:
		return HttpResponse("Name taken")
	if check_mac(mac_address) == 1:
		return HttpResponse("Device already added")
	
	
	known_devices[name] = mac_address
	response = HttpResponse()
	add_to_file()
	print(type(known_devices))
	print(known_devices)
	temp = "added {} with mac of {}"
	
	return HttpResponse(temp.format(name,mac_address))



# this functions takes out devices that are in the our list
def remove_device(request, name):
	if check(name) == 1:
		return HttpResponse("Not in list")
		
	known_devices.pop(name)
	send = "{} was removed"
	response = HttpResponse(send.format(name))
	add_to_file()
	return response


#this function renames devices
def rename_device(request, old_name, new_name):
	if check(new_name) == 0:
		return HttpResponse("name taken")

	if check(old_name) ==1:
		return HttpResponse("device not found") 

	known_devices[new_name] = known_devices[old_name]
	known_devices.pop(old_name)
	add_to_file()
	send = "{} renamed to {}"
	response = HttpResponse(send.format(old_name,new_name))
	return response
	
	
def tt (request,name,position):
	if check(name) == 1:
		return HttpResponse("this is not a known device")
	if position > 180:
		return HttpResponse("too high")
	if position <= 0:
		return HttpResponse("negative")


	#time.sleep(0.5)
	list_to_return = []
	pp = str(position)
	num_variables_to_notify = 2
	
	try:
		ble_scan_object = ble_scan.MyDelegate()
		ble_scan_object.connect("30:AE:A4:25:14:56") 
		ble_scan_object.send_command(pp)
		list_to_return = list(ble_scan_object.check_notifications())
		print(list_to_return)
		ble_scan_object.disconnect()
		tt = "Moved to {}"
		return HttpResponse(tt.format(position))
		
	except:
		return HttpResponse("Error")
	
	'''
	for i in range(num_variables_to_notify):
		list_to_return= list(ble_scan_object.check_notifications())
		print(list_to_return)
	'''



def check(name):
	if name in known_devices:
		return 0
	else:
		return 1

def check_mac(mac):
	for x in known_devices.values():
		if x == mac:
			return 1
	return 0
