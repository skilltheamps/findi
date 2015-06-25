#!/usr/bin/env python3
import subprocess
import pickle
import datetime
from os import listdir

listOfEntries = listdir("./data")
filesSizeZero = 0
listOfZero = ""
#print(listOfEntries)
for each in listOfEntries:
        pageDataFile = open("./data/"+each+"/info", "rb")
        pageData = pickle.load(pageDataFile)
        pageDataFile.close()
        if pageData["size"]>0:
                try:
                        print(each+"----"+" http://"+pageData["address"]+" ---"+pageData["title"]+"---("+str(pageData["size"])+"B)---"+pageData["comment"])
                except:
                        print(each+"----"+" http://"+pageData["address"]+"  READ ERROR")
        else:
                listOfZero += each+"---- http://"+pageData["address"] + "\n"
                filesSizeZero = filesSizeZero+1
print("\nFiles with size zero: "+str(filesSizeZero))
print(listOfZero)
