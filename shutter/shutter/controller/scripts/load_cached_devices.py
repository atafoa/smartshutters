import json
import os
import csv


def load_csv():
	thing={}
	fp = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", "r")
	csvr = csv.DictReader(fp)
	for row in csvr:
		thing[row['name']]= row['mac']
	return thing



d = load_csv()
#d = load_cached_devices()
print(type(d))
print (d)





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











