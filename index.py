import os
import shutil
import time
import threading
print("""
	
	
	      CHAT SYSTEM\n\n                                 - Piyush""")
pass1=str("07A234")	      
def ser():
    
    olddoc = open("mytxtdoc.txt","r")
    olist=olddoc.readlines()
    for i in olist:
        print(i)
    threading.Thread(target =cli).start() 
   
    while True:
        time.sleep(1)
        newdoc = open("mytxtdoc.txt","r")
        nlist=newdoc.readlines()
        if len(olist)!=len(nlist):
            n=len(nlist)-len(olist)
            
            for i in range(n):
                l12=len(us)+1
                if us not in (nlist[len(olist)+i]):
                    print(nlist[len(olist)+i])
        olist=nlist    
    n.close()
    
def cli():
    k = open("mytxtdoc.txt","a")
    global us
    print("--------Old Chats ∆---------\n")
    us = input("Username: ")
    print(" Write Anything and Press Enter to Send\n")
    while True:
        mes= input(" ")    
        if mes=="del":
            open("mytxtdoc.txt","w")    
        else:
            d = open("mytxtdoc.txt","a")       
            d.write(us+":"+" "+mes+"\n")
            d.close()
        
        continue
 
def go():
    tpass =input("Enter Password ")  
    if pass1==(tpass):       
        threading.Thread(target =ser).start()
    else:
        print("Wrong Password\n")
        go()
go()