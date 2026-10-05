import csv
from pathlib import Path

with open ('login_attempts.csv', 'r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
       
    ip_records ={}
    for ip_record in csv_reader:
        ip_address=ip_record["ip_address"]
        status=ip_record["status"]
        username=ip_record["username"]
    
        if ip_address not in ip_records:
            ip_records[ip_address]={'failed':0 , 'success': 0 , 'usernames': set()}      
        if status == "failure":
            ip_records[ip_address]['failed']+=1
            ip_records[ip_address]['usernames'].add(username)        
        elif status =="success":
            ip_records[ip_address]['success']+=1
    
for ip, data in ip_records.items():
    if data["failed"]>2:
        print(f" Warning!!! {ip} is suspiciuous it has {data["failed"]} failed attempts ")
        
            

# print(ip_records)