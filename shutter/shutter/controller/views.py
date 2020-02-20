from django.shortcuts import render
from django.http import HttpResponse

import json
import os

def load_cached_devices():
	d = {}
	return d

known_devices = load_cached_devices()

def position(request, name):
	response = HttpResponse(name)
	return response

def move(request, name, position):
	response = HttpResponse(name + ': ' + str(position))
	return response

def devices(request):
	d = []
	for name, mac_address in known_devices.items():
		d['name'] = name
		d['mac_address'] = mac_address
	
	response = HttpResponse(json.dumps(d))
	return response

def scan(request):
	os.system("python /home/pi/hub-repository/shutter/shutter/controller/scripts/scan_devices.py")
	f = open('/home/pi/hub-repository/shutter/shutter/controller/scripts/scan_results.json', 'r')
	scanned_devices = json.loads(f.read())
	
	response = HttpResponse(scanned_devices)
	return response
	
def add_device(request, name, mac_address):
	known_devices[name] = mac_address
	response = HttpResponse()
	return response

def remove_device(request, name):
	known_devices.pop(name)
	response = HttpResponse()
	return response

def rename_device(request, old_name, new_name):
	known_devices[new_name] = known_devices[old_name]
	known_devices.pop(old_name)
	
	response = HttpResponse()
	return response
