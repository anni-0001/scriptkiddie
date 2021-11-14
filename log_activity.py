from datetime import datetime



# basic lil function that writes to the crontab_logger.txt with the date&time for loop or cron

def basic_write_to_file(filepath):
    x = 0
    myfile = open(filepath, 'a')
    while x < 10:
        myfile.write('\nAccessed on '+ str(datetime.now()))
        x +=1

# for cron specifically - not working yet
def cron_write(filename):
    myfile = open(filename, 'a')
    myfile.write('\nAccessed on '+ str(datetime.now()))


def main():

    # cron_write('crontab_logger.txt')
    basic_write_to_file('/home/anni/projects/scriptkiddie/crontab_logger.txt')
    # cron_write('/home/anni/projects/scriptkiddie/crontab_logger.txt')





main()
