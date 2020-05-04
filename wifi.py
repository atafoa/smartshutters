# 1. install network-manager : sudo apt-get install network-manager
# 2. run the script : sudo python try_network.py


import os

# open and append new wifi information in network file in root
f = open("/etc/wpa_supplicant/wpa_supplicant.conf", "a")

quotation = "\""
### Input ID and password 
wifi_id =  quotation + "Haris's pc" + quotation
password = quotation + "turdburger" + quotation
protocal = "key_mgmt=WPA-PSK"


f.write(
"network={" + "\n" +
"    ssid="+wifi_id+"\n"+
"    psk="+password+"\n"+
"    "+protocal+ "\n}"
)

f.close()

# this command line will help the pi rescan and auto connect with the wifis
os.system("wpa_cli -i wlan0 reconfigure")
