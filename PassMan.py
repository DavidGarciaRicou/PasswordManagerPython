import getpass as gp
import csv
username="root"
password="root"
userpwd=""
userlog=""
reqfile="passwd.csv"
n=1
newline=[]
datatoread=[]
check=False
while userlog!=username or userpwd!=password:
    userlog=input("Username: ")
    userpwd=gp.getpass("Password: ")
if userpwd==password and userlog==username:
    while True:
        while n!="1" and n!="2":
            n=str(input("Do you want to introduce a new username & password (1)? or see the current (2): "))
        if n=="1": 
            fo=open(reqfile,'r')
            data=csv.reader(fo)
            datatoread=list(data)
            while check==False:
                newline.append(input("Introduce platform:"))
                
                for x in range(0,len(datatoread)):
                    platcheck=datatoread[x]
                    plattochk=platcheck[0]
                    if newline[0]==plattochk:
                        print("You already setup an username and password for this platform, please change the name of the platform")
                        check=False
                        newline.pop()
                        break
                try:
                    if newline[0]!=plattochk:
                        check=True
                except:
                    pass
            fo.close
            newline.append(input("Introduce username: "))
            newline.append(input("Introduce password: "))
            datatoread=list(data)
            fo=open(reqfile,'a',newline="") #Open file as append
            data=csv.writer(fo) #data=write data with csv into fo
            data.writerow(newline)
            fo.close
            print("Saved!")
            n="0"
            check=False
            newline=[]
        if n=="2":
            pltoread=input("Pleas introduce the name of the platform you want to see username and password: ")
            fo=open(reqfile,'r',newline="") #r to read; newline="" to prevent empty lines
            data=csv.reader(fo)
            datatoread=list(data)
            for x in range(len(datatoread)):
                if pltoread==datatoread[x[0]]:
                    print("This is your Username: "+datatoread[x[1]]+", and password: "+datatoread[x[2]]+", from the platform: "+datatoread[x[0]])
            n="0"
    