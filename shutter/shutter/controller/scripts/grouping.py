import json
import csv	
temp = {"name":"mac_address"}
fp = open("/home/pi/hub-repository/shutter/shutter/controller/scripts/knowndevs.csv", "r")
csvr = csv.DictReader(fp)
for row in csvr:
	temp[row['name']]= row['mac']

room = input("enter the name of the room\t")
name = input("enter name\t")
mac = input("enter mac\t")
rooms  = {}

#this is how you add to a room
rooms[room] = temp
print(rooms[room])
print("\n")

#this is how you pop from the room
rooms[room].pop("name")
print(rooms)
print("\n")

#this is how you add to a room
rooms[room][name] = mac
print(rooms[room])
print("\n")

#this is how you change the name of shutter in a certain room
rooms[room]["new_name"] = rooms[room][name]
rooms[room].pop(name)
print(rooms)
print("\n")

#this is how you can list the rooms 
print(json.dumps(rooms))
print("\n")

#this is how you can list devices in the room
print(json.dumps(rooms[room]))
print("\n")

thing = {}
#just dump every thing into a file and load from that file json should handle everything
thing = json.loads(json.dumps(rooms))
print(thing)
print("\n")

