# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import os
import time
import bluepy.btle as btle
from bluetooth import *
import bluetooth
from bluetool import Bluetooth
import json



def index(request):
	#scanner = btle.Scanner()
	#devices = scanner.getDevices()
	#time.sleep(3)
	#return render(request,'shutter/index.html')
	#print(devices)
	return HttpResponse("home")
# Create your views here.

def range(request):
	# in here we do task of checking all the bluetooth devices nearby
	#
	#
	d = []
	bt = Bluetooth()
	bt.scan()
	devices = bt.get_available_devices()
	msg = json.dumps(devices)
	return HttpResponse(msg, content_type="application/json")


# this function will send the all the know shutters in the format of name : address from a text file
def known_shutters(request):
	return HttpResponse("this is a list of the known shutters (name : address)")

#this function will be the add shutters to list
def add(request, addr):
	return HttpResponse(addr)

#this is the remove function
def sub(request, name):
	return HttpResponse(name)
#get position of shutter 
def get_position(request, name):
	return HttpResponse("this is the get position function")
	
#this is the open function
def open(request, name):
	return HttpResponse("this is the open function")

#this is the close function
def close(request, name):
	return HttpResponse("this is the close function")

# this is the set postion function where they will pass in the name and the position they want to set
def set_pos(request, name, pos):
	return HttpResponse("the shutter %s and the position %s"%(name,pos))

#this is a test
def tt(request):
	time.sleep(2)
	os.system("python /home/pi/hub-repository/SmartShutters/ble_scan.py")
	return HttpResponse("this is a test")
