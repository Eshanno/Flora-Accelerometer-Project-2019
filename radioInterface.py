import time
import serial
import matplotlib.pyplot as plt
from math import pi,atan2,sqrt,cos,sin
import datetime
import numpy
import scipy
from statistics import mean

class MovementPoints:
    def __init__():
        pass

def turnStringToInt(bytes):
    positive=True
    if bytes[0] =="1":
        positive=False
    if positive:
        theNumber=0
        for bitPos in range(1,len(bytes)):
            if bytes[bitPos]=="1":
                theNumber+=(2**(len(bytes)-1-bitPos))
        return theNumber
    else:
        #negative
        theNumber=0
        for bitPos in range(1,len(bytes)):
            if bytes[bitPos]=="0":
                theNumber+=(2**(len(bytes)-1-bitPos))
        return -1*(theNumber+1)

def takeInfo():
        with serial.Serial('/dev/ttyUSB0',38400, timeout=1) as ser:


            columns=[[],[],[],[],[],[]]
            standStill=[[],[],[],[],[],[]]
            import time

            t0 = time.time()

            #62.5 readings a second not too bad
            for x in range(1000):
                for num in range(6):

                        line = ser.read(2)# read a '\n' terminated line
                        b=""

                        if(line!=b''):


                            for x in line:
                                b=b+(bin(x)[2:].zfill(8))
                            standStill[num].append(b)
            t1 = time.time()
            print("Time Taken To calibrate:",end="")
            print(t1-t0)
            print("Calibrated")
            try:
                while True!=None:

                    for num in range(6):
                        line = ser.read(2)# read a '\n' terminated line
                        b=""
                        if(line!=b''):
                            for x in line:
                                b=b+(bin(x)[2:].zfill(8))
                            columns[num].append(b)

            except Exception as e:
                print("Breaking Loop")
            finally:
                for x in range(len(columns)):
                    #Clear The Data Of Nulls
                    columns[x]=columns[x][5:len(columns[x])-5]
                parseToWorkableNumbers(columns)
                parseToWorkableNumbers(standStill)
                return (columns,standStill)

def parseToWorkableNumbers(array,zero=0):
    for singleCol in range(len(array)):
        for data in range(len(array[singleCol])):
            array[singleCol][data]=turnStringToInt(array[singleCol][data])-zero
    return array

def graphData(columnOfData):
    import matplotlib.pyplot as plt
    plt.plot(columnOfData)
    plt.show()

def exportData(dataSet):
    exportable=[[],[],[],[],[],[]]
    for numRow in range(len(dataSet[0])):
        for numCol in range(len(dataSet)):
            exportable[numCol][numRow]=dataSet[numRow][numCol]
    import csv

    with open(input("File Name to write out to"), "wb") as f:
        writer = csv.writer(f)
        writer.writerows(exportable)

#Move Slow Move Middle Move Fast
def isMoving(columnData):
    tolerenceOfSensor=0
    means=list()
    for x in range(int(len(columnData)/50+1)):
        print(x)
        frameOfData=columnData[x*50:]
        means.append(mean(frameOfData))
    for y in range(len(means)-1):
        if(means[y]+tolerenceOfSensor<means[y+1]):
            print("Going Up")
            ####Rework
        elif(means[y]-tolerenceOfSensor>means[y+1]):
            print("Going Down")
        else:
            print("About The Same")

    plt.plot(means)
    plt.show()
    return(means)
