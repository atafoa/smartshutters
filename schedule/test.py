import smtplib
import urllib2
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

contents = urllib2.urlopen("http://api.aladhan.com/v1/timingsByCity/:date_or_timestamp?city=arlington&country=US").read()
jsonContents = json.loads(contents);

fajr = jsonContents['data']['timings']['Fajr'];
fhour,fmin = fajr.split(":");
dhur = jsonContents['data']['timings']['Dhuhr'];
dhour, dmin = dhur.split(":");
asr =  jsonContents['data']['timings']['Asr'];
ahour,amin = asr.split(":");
magrib = jsonContents['data']['timings']['Maghrib'];
mhour, mmin = magrib.split(":");
isha = jsonContents['data']['timings']['Isha'];
ihour,imin = isha.split(":");


thing = MIMEMultipart();

thing['From'] = "harisqureshi714@gmail.com"
thing['To'] = "2016757203@tmomail.net"
thing['Subject']= "Messages to pray"

body = "time to pray"

thing.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587);

server.ehlo();

server.starttls();


server.login("harisqureshi714@gmail.com","Mahouse1");

msg = thing.as_string()

server.sendmail("harisqureshi714@gmail.com","2016757203@tmomail.net",msg);

server.close();

print("Email was sent to pray")
