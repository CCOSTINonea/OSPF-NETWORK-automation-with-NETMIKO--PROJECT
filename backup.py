from os import write
from netmiko import ConnectHandler
import csv
csv.register_dialect('hashes',delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')
with open('devices_for_backup.csv','r') as csvfile:
    reader=csv.reader(csvfile,dialect='hashes')
    next(reader)
    for row in reader:
        cisco_device = {
            'device_type': 'cisco_ios',
            'host': row[0],
            'username': row[1],
            'password': row[2],
            'port': 22,
            'verbose': True
        }
        connection = ConnectHandler(**cisco_device)
        output = connection.send_command('show run')
        prompt = connection.find_prompt()
        from datetime import datetime
        now=datetime.now()
        month=now.month
        day=now.day
        hour=now.hour
        minute=now.minute

        with open(f"{prompt}-backup_{day}.{month}--{hour}-{minute}.txt",'w') as backup:
            backup.write(output)
        print(output)
        connection.disconnect()
