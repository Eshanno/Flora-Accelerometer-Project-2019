#PySerial
import time
import serial
import matplotlib.pyplot as plt
from math import pi,atan2,sqrt,cos,sin
ser = serial.Serial('/dev/ttyUSB0')




class readingsList:
    def __init__(self ,readings=list()):
        self.readings=readings
    def __str__(self):
        for reading in self.readings:
            print(reading)
    def calcRanges(self):
        sampleReadings=[ y.accel['x'] for y in [x for x in self.readings]]
        xrange=(min(sampleReadings),max(sampleReadings))
        midpoint=((xrange[0]+xrange[1])/2)
        distFromMidpoint=midpoint-xrange[0]
        print(xrange)
        print(distFromMidpoint)
        print(midpoint)
        #About 44 each time
        #TODO CLEAN THAT UPPP DUDE

class sensorReading:

    def __init__ (self,accelDict=dict(),magDict=dict(),gyroDict=dict(),temp=0,timeStamp=None):
        self.accel = accelDict
        self.mag=magDict
        self.gyro=gyroDict
        self.timeStamp=timeStamp
        #Derived Calculations

        self.pitch=self.calcPitch()
        self.roll=self.calcRoll()
        self.mag_x = self.mag['x']*cos(self.pitch) + self.mag['y']*sin(self.roll)*sin(self.pitch) + self.mag['z']*cos(self.roll)*sin(self.pitch)
        self.mag_y = self.mag['y'] * cos(self.roll) - self.mag['z'] * sin(self.roll)
        self.yaw=self.calcYaw()

    def printRaw(self):
        tString=""
        tString+=("Reading Number %d" % (self.timeStamp))
        tString+="\n"

        tString+="Accel:"
        accelList=[(key+":"+str(self.accel[key])) for key in self.accel]
        tString=tString+" ".join(accelList)
        tString+="\n"

        tString+="Mag:"
        magList=[(key+":"+str(self.mag[key])) for key in self.mag]
        tString=tString+" ".join(magList)
        tString+="\n"

        tString+="Gyro:"
        gyroList=[(key+":"+str(self.gyro[key])) for key in self.gyro]
        tString=tString+" ".join(gyroList)
        tString+="\n"

        return(tString)
    def __str__(self):
        tString=""
        tString+=("Reading Number %d" % (self.timeStamp))
        tString+="\n"
        tString+=("Pitch:%d Roll%d Yaw%d" % (self.pitch,self.roll,self.yaw))
        tString+="\n"
        return(tString)
    def calcPitch(self):
        pitch = 180 * atan2(self.accel['x'], sqrt(self.accel['y']*self.accel['y'] + self.accel['z']*self.accel['z']))/pi
        return pitch
    def calcRoll(self):
        roll = 180 * atan2(self.accel['y'], sqrt(self.accel['x']*self.accel['x'] + self.accel['z']*self.accel['z']))/pi
        return roll
    def calcYaw(self):
        yaw = 180 * atan2(-self.mag_y,self.mag_x)/pi;
        return yaw


#Trade readability for speed
def parseToReading(lineBytes):
    readingString=lineBytes.decode('UTF-8')
    readingString=readingString.strip('[\n\r]')
    listOfInts=readingString.split(",")
    listOfInts=[int(num) for num in listOfInts]
    # ACCEL X Y ZMAG X Y Z GYRO X Y Z TEMP= num
    reading=sensorReading({'x':listOfInts[0],'y':listOfInts[1],'z':listOfInts[2]},{'x':listOfInts[3],'y':listOfInts[4],'z':listOfInts[5]},{'x':listOfInts[6],'y':listOfInts[7],'z':listOfInts[8]},listOfInts[9],time.time())
    return(reading)


def calibrateTolerences():
    with serial.Serial('/dev/ttyUSB0',34800, timeout=1) as ser:
        readings=readingsList()
        count=0
        while ser.readline()!=None and count<30:
            print(count)
            line = ser.readline()   # read a '\n' terminated line
            reading=parseToReading(line)
            readings.readings.append(reading)
            count+=1
        readings.calcRanges()
        input("Waiting...")

## Main ##
#calibrateTolerences()
with serial.Serial('/dev/ttyUSB0',34800, timeout=1) as ser:
    readings=readingsList()
    while ser.readline()!=None:
        line = ser.read(2)   # read a '\n' terminated line
        #reading=parseToReading(line)
        #readings.readings.append(reading)
        print(line)
