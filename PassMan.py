import getpass as gp
import base64 as b6
import csv,sys
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
        while n!="1" and n!="2" and n!="3":
            n=str(input("Do you want to introduce a new username & password (1), or see the current (2) and if you want to leave (3): "))
        if n=="3":
            sys.exit("Thanks for using this program :)")
        if n=="1": 
            fo=open(reqfile,'r')
            data=csv.reader(fo)
            datatoread=list(data)
            while check==False:
                newline.append(input("Introduce platform, if you want to go back input (0): "))
                if newline[0]=="0":
                    check=True
                if newline[0]!="0":
                    for x in range(0,len(datatoread)):
                        platcheck=datatoread[x]
                        plattochk=platcheck[0]
                        if newline[0]==plattochk:
                            print("You already setup an username and password for this platform, please change the name of the platform: ")
                            check=False
                            newline.pop()
                            break
                    try:
                        if newline[0]!=plattochk:
                            check=True
                    except:
                        pass
            if newline[0]!="0":
                fo.close
                newline.append(input("Introduce username: "))
                newline.append(gp.getpass("Introduce password: "))
                for x in range(1,len(newline)):
                    newline[x]=(b6.b64encode(str.encode(newline[x])))
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
            while check==False:
                pltoread=input("Pleas introduce the name of the platform you want to see username and password, or (all) to show them all: ")
                fo=open(reqfile,'r',newline="") #r to read; newline="" to prevent empty lines
                data=csv.reader(fo)
                datatoread=list(data)
                platcheck=[]
                aux=[]
                if pltoread=="all":
                    for x in range(1,len(datatoread)):
                        platcheck=datatoread[x]
                        print("Platform: ",platcheck[0])
                        print("Username: ",(b6.b64decode((platcheck[1])[2:-1:])).decode("utf-8"))
                        print("Password: ",(b6.b64decode((platcheck[2])[2:-1:])).decode("utf-8"))
                        print("=======================")
                    check=True
                elif pltoread!="all":
                    for x in range(len(datatoread)):
                        platcheck=datatoread[x]
                        plattochk=platcheck[0]
                        if pltoread==plattochk:
                            print("Platform: ",platcheck[0])
                            print("Username: ",(b6.b64decode((platcheck[1])[2:-1:])))
                            print("Password: ",(b6.b64decode((platcheck[2])[2:-1:])))
                            print("=======================")
                            c=True
                            break
                    if c!=True:
                        print("Platform not found on the database, check for (all)")
                n="0"
            check=False
