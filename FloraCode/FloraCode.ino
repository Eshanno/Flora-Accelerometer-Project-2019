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
byte accelx = 0;
byte accely = 1;
byte accelz = 2;
byte magx = 3;
byte magy = 4;
byte magz = 5;

void setup()
{
  // Baud rate MUST match XBee settings (as set in XCTU)

  XBee.begin(38400);
  Serial.begin(9600);
  lsm.begin();
  while(Serial.available()<=0){
    Serial.println("Wait");
    delay(5);

  }
  Serial.println("GOING!");
  //{
    //XBee.println("Oops ... unable to initialize the LSM9DS0. Check your wiring!");
    //while (1);
  //}
  //XBee.println("Found LSM9DS0 9DOF");
  //XBee.println("");
  //XBee.println("");
}

void loop()
{
  lsm.read();
  short accelx = lsm.accelData.x; short accely=lsm.accelData.y;short accelz=lsm.accelData.z;
  short magx=lsm.magData.x ; short magy=lsm.magData.y ; short magz= lsm.magData.z;
  Serial.println(accelx);Serial.print("\t");Serial.print(accely);Serial.print("\t");Serial.print(accelz);Serial.print("\t");Serial.print(magx);Serial.print("\t");Serial.print(magy);Serial.print("\t");Serial.print(magz);Serial.print("\n");
  // ACCEL X 
  byte shortArray[]={highByte(accelx),lowByte(accelx)};
  XBee.write(shortArray,2);
  // ACCEL Y 
  byte shortArray1[]={highByte(accely),lowByte(accely)};
  XBee.write(shortArray1,2);
  // ACCEL Z
  byte shortArray2[]={highByte(accelz),lowByte(accelz)};
  XBee.write(shortArray2,2);
  // MAG X
  byte shortArray3[]={highByte(magx),lowByte(magx)};
  XBee.write(shortArray3,2);
  // MAG Y
  byte shortArray4[]={highByte(magy),lowByte(magy)};
  XBee.write(shortArray4,2);
  // MAG Z
  byte shortArray5[]={highByte(magz),lowByte(magz)};
  XBee.write(shortArray5,2);
  
 
  

}
