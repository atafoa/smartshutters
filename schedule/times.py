from crontab import CronTab
import datetime
import urllib2
import json

contents = urllib2.urlopen("http://api.aladhan.com/v1/timingsByCity/:date_or_timestamp?city=arlington&country=US").read()
jsonContents = json.loads(contents);

fajr = jsonContents['data']['timings']['Fajr'];
fhour,fmin = fajr.split(":"); #tokenize string
dhur = jsonContents['data']['timings']['Dhuhr'];
dhour, dmin = dhur.split(":");
asr =  jsonContents['data']['timings']['Asr'];
ahour,amin = asr.split(":");
magrib = jsonContents['data']['timings']['Maghrib'];
mhour, mmin = magrib.split(":");
isha = jsonContents['data']['timings']['Isha'];
ihour,imin = isha.split(":");

print (fajr)
print (dhur)
print (asr)
print (magrib)
print (isha)

f = open("/home/pi/Desktop/dates.txt", 'r')
msg = f.read();
print (msg);
f.close



#creating new cron jobs
my_cron = CronTab(user = "pi");

#setting the command on the job
job = my_cron.new(command = 'sudo python /home/test.py');


#job.hour.on(fhour);
now = datetime.datetime.now();

#convert the times to int becuase they strings right now
min = int(fmin);
hour = int(fhour);

Dmin_int = int(dmin);
Dhour_int = int(dhour);

Asr_min_int = int(amin);
Asr_hour_int = int(ahour);

mmin_int = int(mmin);
mhour_int = int(mhour);

imin_int = int(imin);
ihour_int = int(ihour);

day = int(now.day);
month= int(now.month);

#set the time for fajr

job.setall(min,hour,day,month,'*','*');



#enable the job

job.enable();


#write the job to the file
my_cron.write();
print("program wrote fajr");

#After making the first job make the next so on and so fourth

cron2 = CronTab(user = "pi");
Dhur = cron2.new(command = 'sudo pyhton /home/test.py');
Dhur.setall(Dmin_int,Dhour_int,day,month,'*','*');
Dhur.enable();
cron2.write();
print("program wrote dhur");


cron3 = CronTab(user = "pi");
Asr = cron3.new(command = 'sudo python /home/test.py');
Asr.setall(Asr_min_int,Asr_hour_int,day,month,'*','*');
Asr.enable();
cron3.write();
print("program wrote asr");


cron4 = CronTab(user = "pi");
M = cron4.new(command = 'sudo python /home/test.py');
M.setall(mmin_int,mhour_int,day,month,'*','*');
M.enable();
cron4.write();
print("program wrote majrib");



cron5 = CronTab(user = "pi");
I = cron5.new(command = 'sudo python /home/test.py');
I.setall(imin_int,ihour_int,day,month,'*','*');
I.enable();
cron5.write();
print("program wrote isha");

