import os,shutil,datetime

#Properties
destination="C:/Users/Subhasish/Desktop/JOB SHEET"
backupLocation="D:/SUBHASISH/JOB SHEET"
MainFile="JOB SHEET.xlsx"
source=destination+"/JOB SHEET/"+MainFile
NewFile=""

#This Dictionary is used to store lot number as a key and file name as a value.
Lots={}

#Main function 
def main():
    LotNum()
    print(destination)
    x=0
    for z in os.listdir(destination):
        if z.startswith("["):
            start=z.find("[")+1
            end=z.find("]")
            slnum=int(z[start:end])
            if x<slnum:x=slnum

    print(f"Last sl number was {x}, new one is {x+1}")
    serial_no=x+1
    lotNumber=input("Enter LotNumber->")
    lotNumber=lotNumber.replace(" ","").lower()
    if lotNumber not in Lots.keys():
        shutil.copy(source,destination)
        NewFile=f"[{serial_no}] {lotNumber}.xlsx"
        os.rename(destination+"/"+MainFile,destination+"/"+NewFile)
        
        #To creat a logs of Every Creation
        Logs(f"{NewFile} Created")

        os.startfile(destination+"/"+NewFile)
        backupBool=input("Do you want to backup?(y/n)\n->>")
        if input.lower()=="y":
            Backup()
            print("Backup sucessfull.")
        else:
            print("Closing without Backup!")
    else:
        print("Lot already Exists!",Lots[lotNumber])


#Rename function for slice and rename a file name
def rename():
    for z in os.listdir(destination):
        if not z.startswith("~") and  z.__contains__("."):
            num=z.split(" ")[0]
            num1=z.split(" ")[1:]
            num="".join(x for x in num)
            num1="".join(x for x in num1)
            os.rename(destination+"/"+z,destination+"/"+f"[{num}] {num1}")

#For not Creat Same Lot Again
def LotNum():
    for z in os.listdir(destination):
        if(z.startswith("[")):
            name,ext=os.path.splitext(z)
            startIndex=name.find("]")+2
            name=name[startIndex:]
            Lots[name]=z

#Creating Logs is Always helpfull
def Logs(FileName):
    with open(f"{destination}/Logs/Logs.txt","a") as logs:
        logs.write(f"{FileName} {datetime.datetime.now()}\n")
        logs.close()

#For Backup All data
def Backup():
        try:
            shutil.rmtree(backupLocation)
            shutil.copytree(destination,backupLocation)
        except FileExistsError:pass
        except Exception as e:
            print(e)


main()