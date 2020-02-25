
known_devices = [{"name": "thing2", "mac_address": "2"},{"name": "thing1", "mac_address": "1"},{"name": "thing3", "mac_address": "3"}]
def add_to_file():
    f = open("/home/pi/Desktop/hub-repository/shutter/shutter/controller/scripts/known_devices.json",'w+')
    thing = {}
    d = {}
    for name, mac_address in known_devices.items():
	    d['name'] = name
	    d['mac_address'] = mac_address
    f.write(json.dumps(d))
    f.close()

