# A menu in a loop: Add entry, View entries, Weekly summary, Quit
# Add entry asks for the habit (e.g. “Python”), minutes spent, and uses today’s date automatically
# Entries are saved to a file (use JSON) so they survive closing the program
# On startup, the program loads the saved entries (and starts empty if the file doesn’t exist yet)
# View entries prints everything, newest first
# Weekly summary shows total minutes per habit for the last 7 days



import json
import datetime
from datetime import date , timedelta


#load saved entries, start empty if file is missing or broken
try:
    with open("data.json", "r") as file:
        entries=json.load(file)
        
except (FileNotFoundError , json.JSONDecodeError) :
    entries=[]
 
print("Task-Tracker")   
    

while True:
#Get user input about their choice
    choice=input("Please choose, Type A to: Add | V to: View | S to: Summuray |Q to: Quit : ").strip().lower()
   #for user to add task,minutes if they choose A
    if choice=="a":
        task=input("Task: ").strip()
        try:
            minu=input("Minutes: ")
            minutes=int(minu)
        except ValueError:
            print("The minutes must be a number")
            continue
        #add the user input in a dict.  
        entry={
          "Date": str(datetime.date.today()),
          "Task" : task ,
          "Minutes": minutes    
        }
        
        
        #save every entry to the entries list 
        entries.append(entry)  
    
        #saves entries in the json file
        with open("data.json", "w") as file:
            json.dump(entries,file, indent=4)
    
    elif choice=="v":
        if not entries:
            print("No Task saved yet.")
            continue
        #print each entry inside entries
        for entry in entries:
            print(f"{entry ['Date']}, {entry['Task']},{entry['Minutes']}")
    elif choice=="q":
        print("keep Going, another good grindDay, See ya ")
        break
       
    elif choice=="s":
        #create a vrariable that store the user input store in entry so that we can do the math and print  
        time_totals={}
        today_date=datetime.date.today()
        cutof_date=today_date-timedelta(days=7)
        
        
        for entry in entries:
            user_date=entry['Date']
            iso_date=date.fromisoformat(user_date)
            task=entry['Task']
            minutes=entry['Minutes']
            if iso_date>=cutof_date:
                #if the task is not in the dict yet get() return 0, then add minutes
                time_totals[task]=time_totals.get(task, 0) + minutes
        #.items get key and value of time_totavls
        for key, value in time_totals.items():
            print(f"{key}, {value} min")
                   
    else :
        print("Please press A,V,S or Q")
        continue
    
        
            
    