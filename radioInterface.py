#PySerial
import time
import serial
import matplotlib.pyplot as plt
from math import pi,atan2,sqrt,cos,sin
import datetime
from array import array
import numpy
import scipy
#ser = serial.Serial('/dev/ttyUSB0')

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




class Rotaitons:
    def calcPitch(self):
        pitch = 180 * atan2(self.accela['x'], sqrt(self.accel['y']*self.accel['y'] + self.accel['z']*self.accel['z']))/pi
        return pitch
    def calcRoll(self):
        roll = 180 * atan2(self.accel['y'], sqrt(self.accel['x']*self.accel['x'] + self.accel['z']*self.accel['z']))/pi
        return roll
    def calcYaw(self):
        return yaw
        yaw = 180 * atan2(-self.mag_y,self.mag_x)/pi;
def takeInfo():
        with serial.Serial('/dev/ttyUSB0',38400, timeout=1) as ser:

            columns=[[],[],[],[],[],[]]
            ser.write(b'Hello')
            standStill=[[],[],[],[],[],[]]
            for x in range(2000):
                for num in range(6):
                        line = ser.read(2)# read a '\n' terminated line
                        b=""
                        for x in line:
                            b=b+(bin(x)[2:].zfill(8))
                        standStill[num].append(b)
            print("Calibrated")
            try:
                while True!=None:

                    for num in range(6):
                        line = ser.read(2)# read a '\n' terminated line
                        b=""
                        for x in line:
                            b=b+(bin(x)[2:].zfill(8))
                        columns[num].append(b)

            except Exception as e:
                print("Breaking Loop")
            finally:
                for x in range(len(columns)):
                    #Clear The Data Of Nulls
                    columns[x]=columns[x][5:len(columns[x])-5]
                return (columns,standStill)
def parseToWorkableNumbers(array,zero=0):
    for singleCol in range(len(array)):
        for data in range(len(array[singleCol])):
            array[singleCol][data]=turnStringToInt(array[singleCol][data])-zero


    return array





            #print(a)

            #print(time.localtime( time.time() ))
