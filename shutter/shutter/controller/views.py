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

def load_rooms():
	fp = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/rooms.json","r")
	thing = json.load(fp)
	print(thing)
	return thing

rooms = load_rooms()

def add_to_file():
    csv_fp = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", mode='w').close()
    csv_fp = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", mode='w')
    feilds = ['name','mac']
    writer = csv.DictWriter(csv_fp,fieldnames=feilds)
    writer.writeheader()
    for name, mac_address in known_devices.items():
    	print(name,mac_address)
    	writer.writerow({'name':name,'mac':mac_address})


def add_room_to_file():
	fp = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/rooms.json","w").close()
	fp = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/rooms.json","w")
	fp.write(json.dumps(rooms))
	fp.close()

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
	
	response = HttpResponse(json.dumps(scanned_devices))
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
	for room in rooms:
		if name in rooms[room]:
			rooms[room].pop(name)
	add_room_to_file()
	
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
	for room in rooms:
		if old_name in rooms[room]:
			rooms[room][new_name] = rooms[room][old_name]
			rooms[room].pop(old_name)
	send = "{} renamed to {}"
	response = HttpResponse(send.format(old_name,new_name))
	return response
	
	
#this function will add devices to a group
def create_room(request, name):
	empty = {}
	if name in rooms:
		return HttpResponse("Already in rooms")
	rooms[name] = empty
	add_room_to_file()
	return HttpResponse("added "+name+" room")
	

def list_rooms(request):
	d = {}
	l = []
	for e,dd in rooms.items():
		d['room'] = e
		for name,mac in dd.items():
			d['name'] = name
			d['mac'] = mac
			l.append(dict(d))
	return HttpResponse(json.dumps(l))

def list_rooms_only(request):
	d = {}
	l = []
	for e, dd in rooms.items():
		d['room'] = e
		l.append(dict(d))
	return HttpResponse(json.dumps(l))

def list_room_shutters(request, room):
	d = {}
	l = []
	for e, dd in rooms[room].items():
		d['name'] = e
		d['mac_address'] = dd
		l.append(dict(d))
	return HttpResponse(json.dumps(l))

def delete_room(request,room):
	if room not in rooms:
		return HttpResponse("not a room")
	rooms.pop(room)
	return HttpResponse("removed "+room)

def rename_room(request,old_room,new_room):
	if old_room not in rooms:
		return HttpResponse("Not a room")
	if new_room in rooms:
		return HttpResponse("Already in room")
	rooms[new_room] = rooms[old_room]
	rooms.pop(old_room)
	return HttpResponse("Success fully renamed room")

def add_to_room(request,room,shutter):
	if shutter not in known_devices:
		return HttpResponse("You have to add the shutter first")
	if room not in rooms:
		return HttpResponse("You have to create the room first")
	if shutter in rooms[room]:
		return HttpResponse("The shutter is already in the room")
	rooms[room][shutter] = known_devices[shutter]
	add_room_to_file()
	return HttpResponse("Added "+shutter+" to room "+room)
	
def remove_from_room(request,room,shutter):
	if shutter not in known_devices:
		return HttpResponse("Unknown shutter")
	if room not in rooms:
		return HttpResponse("Unkown room")
	if shutter not in rooms[room]:
		return HttpResponse("Device not in room")
	rooms[room].pop(shutter)
	add_room_to_file()
	return HttpResponse("Device was successfully deleted")


#this is just a test url if we need to test any method or function we do it here 
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


#controller\devices\schedule\name of shutter or group\position\min,hour,day of week (sunday(0,7)-saturday(6)\day of month\month)
def schedule(request,group,position,minutes,hour,day_of_week,DOM,month):
	
	oof = "python /home/pi/hub-repository/shutter/shutter/controller/scripts/set_time.py {} {} {} {} {} {} {}"
	send_min = str(minutes)
	send_hr = str(hour)
	send_day = str(day_of_week)
	send_dom = str(DOM)
	send_month = str(month)
	
	if minutes == 666:
		send_min = "*"

	elif minutes >= 60 or minutes < 0:
		return HttpResponse("incorrect minutes")
	
	if hour == 666:
		send_hr = "*"
	
	elif hour >= 24 or hour < -1:
		return HttpResponse("incorrect hour")
	
	if day_of_week == 666:
		send_day = "*"
	
	elif day_of_week >7 or day_of_week < -1:
		return HttpResponse("incorrect day of week")
	
	if DOM == 666:
		send_dom = "*"
	
	
	elif DOM >31 or DOM <0:
		return HttpResponse("incorrect date")
	
	if month == 666:
		send_month = "*"
		
	elif month >12 or month <1:
		return HttpResponse("incorrect month")
	
	if group  in known_devices:
		#oof = "python /home/pi/hub-repository/shutter/shutter/controller/scripts/set_time.py "+known_devices[group]+" "+position
		os.system(oof.format(send_min, send_hr,send_day,send_dom,send_month,known_devices[group],position))
		return HttpResponse(oof.format(send_min, send_hr,send_day,send_dom,send_month,known_devices[group],position))
		
	#we have to do it for the group now so if they send a room
	#then we have to set the schedule for each shutter therefore an os command for each shutter 
	#idk if we can send alot within a few seconds
	elif group in rooms:
		
		return HttpResponse(oof.format(send_min, send_hr,send_day,send_dom,send_month,rooms[group],position))
	
	
	ans = "{} {} {} {} {}"
	return HttpResponse(ans.format(group,position,minutes,hour,day_of_week))






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
