from bluetool import Bluetooth

import json

d = []

bt = Bluetooth()
bt.scan()
devices = bt.get_available_devices()

f = open('/home/pi/hub-repository/shutter/shutter/controller/scripts/scan_results.json', 'w+').close()

f = open('/home/pi/hub-repository/shutter/shutter/controller/scripts/scan_results.json', 'w+')
f.write(json.dumps(devices))
f.close()
