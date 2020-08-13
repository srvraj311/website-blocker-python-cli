# Website Blocker

# Windows 'C:\Windows\System32\drivers\hosts'
# Linux /etc/hosts
import time
from datetime import datetime as dt

#Change time of day, when to block

time_to_start = 0  # Hours in 24hrs format
time_to_end =  10 # Hours in 24hrs format

# Change Your refresh frequency 
freq = 5 # in seconds


# Change your OS on line starting with 'WITH'


linux_hosts_path = '/etc/hosts'
windows_host_path = 'C:\Windows\System32\drivers\hosts'


redirect = '127.0.0.1'

# Add yur wesites here , seperated by comma

websites_list = ['www.facebook.com', 'facebook.com']


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, time_to_start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, time_to_end):
        print('Working Hours')
        
        # Checking the file for hostnames
        
        with open(linux_hosts_path, 'r+') as file:
            content = file.read()
            for item in websites_list:
                if item not in content:
                    file.write(str(redirect+ ' ' + item + '\n'))
                else:
                    pass
        
    else:
        with open(linux_hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print('Not Working Hour')
        

    time.sleep(freq)

