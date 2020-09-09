import getpass as gp
import csv
username="root"
password="root"
userpwd=""
userlog=""
reqfile="passwd.csv"
n=1
newline=[]
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
            print(datatoread)
            while check==False:
                newline.append((input("Introduce platform: ").lower))
                for x in range(len(datatoread)):
                    if newline[0]==datatoread[x[0]]:
                        print("You already setup an username for this platform, if you want to add another change the platform name for example (platform1)")
                        check=False
                    else:
                        check=True
            newline.append(input("Introduce username: "))
            newline.append(input("Introduce password: "))
            fo.close
            datatoread=list(data)
            fo=open(reqfile,'a') #Open file as append
            data=csv.writer(fo) #data=write data with csv into fo
            data.writerow(newline)
            fo.close
            break
        if n=="2":
            pltoread=input("Pleas introduce the name of the platform you want to see username and password: ")
            fo=open(reqfile,'r',newline="") #r to read; newline="" to prevent empty lines
            data=csv.reader(fo)
            datatoread=list(data)
            for x in range(len(datatoread)):
                if pltoread==datatoread[x[0]]:
                    print("This is your Username: "+datatoread[x[1]]+", and password: "+datatoread[x[2]]+", from the platform: "+datatoread[x[0]])
            break
    