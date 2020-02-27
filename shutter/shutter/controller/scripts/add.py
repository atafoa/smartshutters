import json
import csv

known_devices = {'thing1':'1','thing2':'2', 'thing3':'3'}



def add_csv():
    csv_fp = open("knowndevs.csv", mode='w')
    feilds = ['name','mac']
    writer = csv.DictWriter(csv_fp,fieldnames=feilds)
    writer.writeheader()
    for name, mac_address in known_devices.items():
	print(name,mac_address)
	writer.writerow({'name':name,'mac':mac_address})
	
	
	
add_csv()
print("done\n")
