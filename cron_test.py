from crontab import CronTab

# cron = CronTab(user='root')
# job = cron.new(command)
cron = CronTab(user='anni')
# job = cron.new(command='python3 log_activity.py')
job = cron.new(command='python3 /home/anni/projects/scriptkiddie/log_activity.py')
job.minute.every(1)

cron.write()




# with CronTab( user = 'root') as cron:
#     job = cron.new(command= 'echo hello world')
#     job.minute.every(1)
# print('cron.write() was just executed')

