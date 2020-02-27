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


