import json
import csv
temp = {"name":"mac_address"}
room = input("enter the name of the room\t")
name = input("enter name\t")
mac = input("enter mac\t")
rooms  = {}

#this is how you add to a room
rooms[room] = temp
print(rooms[room])

#this is how you pop from the room
rooms[room].pop("name")
print(rooms)

#this is how you add to a room
rooms[room][name] = mac
print(room[room])

#this is how you change the name of shutter in a certain room
rooms[room]["new_name"] = rooms[room][name]
rooms[room].pop(name)
print(rooms)

#this is how you can list the rooms 
print(json.dumps(rooms))

#this is how you can list devices in the room
print(json.dumps(rooms[room]))

thing = {}
#just dump every thing into a file and load from that file json should handle everything
thing = json.loads(json.dumps(rooms))
