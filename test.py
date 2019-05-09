#PySerial
import time
import serial
import matplotlib.pyplot as plt
from math import pi,atan2,sqrt,cos,sin
import datetime
from array import array
import numpy
import scipy

with serial.Serial('/dev/ttyUSB0',38400, timeout=1) as ser:
    columns=[[],[],[],[],[],[]]
    while(True):
        
        c=ser.read(12)
        print(c)
