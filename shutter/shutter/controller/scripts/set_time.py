from crontab import CronTab
import sys


minute = sys.argv[1]
hour = sys.argv[2]
day_of_week = sys.argv[3]
DOM = sys.argv[4]
month = sys.argv[5]
mac = sys.argv[6]
position = sys.argv[7]



cron = CronTab(user='pi')

oof = 'python /home/pi/hub-repository/shutter/shutter/controller/scripts/task.py '+mac+' '+position
#print(oof)

job = cron.new(command = oof )

#job = cron.new(command='echo hello_world')
job.enable()
cron.write()
'''
for jobs in cron.lines:
	print(jobs)
	print("\n")
#job.enable()
#cron.remove_all()


cron.remove(job)
cron.write()
'''
