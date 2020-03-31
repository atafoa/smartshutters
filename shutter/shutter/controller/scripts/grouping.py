import json
import csv
temp = {"name":"mac_address"}
room = input("enter the name of the room\t")
name = input("enter name\t")
mac = input("enter mac\t")
group  = {}

#this is how you add to a room
group[room] = temp
print(group[room])

#this is how you pop from the room
group[room].pop("name")
print(group)

#this is how you add to a room
group[room][name] = mac
print(group[room])

#this is how you change the name of shutter in a certain room
group[room]["new_name"] = group[room][name]
group[room].pop(name)
print(group)

#this is how you can list the rooms 
print(json.dumps(group))

#this is how you can list devices in the room
print(json.dumps(group[room]))

thing = {}
#just dump every thing into a file and load from that file json should handle everything
thing = json.loads(json.dumps(group))
