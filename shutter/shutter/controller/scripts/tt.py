def tt (request,name,position):
	#time.sleep(2)
	#os.system("python /home/pi/hub-repository/SmartShutters/ble_scan.py")
	list_to_return = []
	list_to_return.clear()
	print(list_to_return)
	pp = str(position)
	num_variables_to_notify = 2
	ble_scan_object = ble_scan.MyDelegate()
	ble_scan_object.connect("30:AE:A4:25:14:56") 
	ble_scan_object.send_command(pp)
	print(type(ble_scan_object.check_notifications()))
	#print(ble_scan_object.check_notifications())
	'''
	for i in range(num_variables_to_notify):
		list_to_return.insert(i,ble_scan_object.check_notifications())
		print(i)
		list_to_return.append(ble_scan_object.check_notifications())
		print("\n")	
	'''
	list_to_return.append(ble_scan_object.check_notifications())
	if len(list_to_return) > 2:
		print("the list is greater then 2")
	
	ble_scan_object.disconnect()
	tt = "you moved {} this far {}"
	#print(ble_scan_object.check_notifications())
	return HttpResponse(list_to_return)


