import os
import json

f = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/known_devices.json", "r+")
thing = json.loads(f.read())
oof ={}


print(thing)