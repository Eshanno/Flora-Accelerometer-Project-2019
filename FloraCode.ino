/* Input-side (button) Arduino code */
#include "SoftwareSerial.h"
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_LSM9DS0.h>
#include <Adafruit_Sensor.h> 
#include <math.h>
#define   M_PI   3.14159265358979323846 /* pi */
Adafruit_LSM9DS0 lsm = Adafruit_LSM9DS0();

void setupSensor()
{
  // 1.) Set the accelerometer range
  lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_2G);
  //lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_4G);
  //lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_6G);
  //lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_8G);
  //lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_16G);
  
  // 2.) Set the magnetometer sensitivity
  lsm.setupMag(lsm.LSM9DS0_MAGGAIN_2GAUSS);
  //lsm.setupMag(lsm.LSM9DS0_MAGGAIN_4GAUSS);
  //lsm.setupMag(lsm.LSM9DS0_MAGGAIN_8GAUSS);
  //lsm.setupMag(lsm.LSM9DS0_MAGGAIN_12GAUSS);

  // 3.) Setup the gyroscope
  lsm.setupGyro(lsm.LSM9DS0_GYROSCALE_245DPS);
  //lsm.setupGyro(lsm.LSM9DS0_GYROSCALE_500DPS);
  //lsm.setupGyro(lsm.LSM9DS0_GYROSCALE_2000DPS);
}

// RX: Arduino pin 2, XBee pin DOUT.  TX:  Arduino pin 3, XBee pin DIN
SoftwareSerial XBee(0, 1);
int BUTTON = 8;
byte pitch = 0;
byte roll = 4;
byte yaw = 8;

void setup()
{
  // Baud rate MUST match XBee settings (as set in XCTU)

  XBee.begin(38400);
   if (!lsm.begin())
  {
    XBee.println("Oops ... unable to initialize the LSM9DS0. Check your wiring!");
    while (1);
  }
  XBee.println("Found LSM9DS0 9DOF");
  XBee.println("");
  XBee.println("");
}

void loop()
{
  lsm.read();
  
  XBee.print((int)lsm.accelData.x); 
  
  XBee.print(","); XBee.print((int)lsm.accelData.y);      
  XBee.print(","); XBee.print((int)lsm.accelData.z);    
  XBee.print(","); XBee.print((int)lsm.magData.x);    
  XBee.print(","); XBee.print((int)lsm.magData.y);         
  XBee.print(","); XBee.print((int)lsm.magData.z);       
  XBee.print(","); XBee.print((int)lsm.gyroData.x);   
  XBee.print(","); XBee.print((int)lsm.gyroData.y);       
  XBee.print(","); XBee.print((int)lsm.gyroData.z);     
  XBee.print(","); XBee.println((int)lsm.temperature);   
  delay(1);

}
