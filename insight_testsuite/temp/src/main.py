from __future__ import division
import math
import os

def PrintOut(RecipientName, RecipientTransList, Percentile):
    FilePath = "../output/repeat_donors.txt"
    Num = int(math.ceil(Percentile/100*len(RecipientTransList))) -1
    with open(FilePath,"a+") as f:
        f.write(RecipientName+"|"+str(RecipientTransList[Num])+"|"+str(sum(RecipientTransList))+"|"+str(len(RecipientTransList))+"\n")
        f.close()
    return


os.chdir("./src")
if os.path.exists("../output/repeat_donors.txt"):
    os.remove("../output/repeat_donors.txt")
FilePath1 = "../input/itcont.txt"
FilePath2 = "../input/percentile.txt"
with open(FilePath1, "r") as f1:
    with open(FilePath2, "r") as f2:
        Percentile = int(f2.readline())
        Line = f1.readline()
        DonatorDict = {}
        RecipientDict = {}
        while Line:
            LineInList = [x.strip() for x in Line.split("|")]
            Recipient = LineInList[0]+"|"+LineInList[10][0:5]+"|"+LineInList[13][4:8]
            Donator = LineInList[7]+"|"+LineInList[10][0:5]
            if DonatorDict.has_key(Donator):
                if RecipientDict.has_key(Recipient):
                    RecipientDict[Recipient].append(int(LineInList[14]))
                    RecipientDict[Recipient].sort()
                    PrintOut(Recipient, RecipientDict[Recipient], Percentile)
                else:
                    RecipientDict[Recipient]= [int(LineInList[14])]
                    PrintOut(Recipient, RecipientDict[Recipient], Percentile)            
            else:
                DonatorDict[Donator] = True
            Line = f1.readline()
