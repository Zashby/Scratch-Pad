#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BMP3XX.h"

#define BMP_SCK 13
#define BMP_MISO 12
#define BMP_MOSI 11
#define BMP_CS 10

// Note: Consider finding your current sealevel pressure to make sensor more accurate. Would make testing easier ;D

#define SEALEVELPRESSURE_HPA (1013.25)

int firingPin = 3;

bool fireReady = false;

Adafruit_BMP3XX bmp;

void setup() {
  
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Adafruit BMP388 / BMP390 test");

  //if (!bmp.begin_I2C()) {   // hardware I2C mode, can pass in address & alt Wire
  if (! bmp.begin_SPI(BMP_CS)) {  // hardware SPI mode  
  //if (! bmp.begin_SPI(BMP_CS, BMP_SCK, BMP_MISO, BMP_MOSI)) {  // software SPI mode
    Serial.println("Could not find a valid BMP3 sensor, check wiring!");
    while (1);
  }

  // Set up oversampling and filter initialization
  bmp.setTemperatureOversampling(BMP3_OVERSAMPLING_8X);
  bmp.setPressureOversampling(BMP3_OVERSAMPLING_4X);
  bmp.setIIRFilterCoeff(BMP3_IIR_FILTER_COEFF_3);
  bmp.setOutputDataRate(BMP3_ODR_50_HZ);




  // setting digital pin mod, declaring set integer values for starting Altitude and what change in altitude you are looking for. Supposedly, with the test pressure it can be accurate to within ten meters.
  // Note: probably want to set targetChange lower for testing purposes, but probably not <10 meters.
  pinMode(firingPin, OUTPUT);
  
  
  // Commented out while working around stupid functions
  // int startAltitude = bmp.readAltitude(SEALEVELPRESSURE_HPA);
  // int targetChange = 1000


  // Hopefully this will delay the change state long enough before it goes through the sensing process.

  delay(2000);

  fireReady = true;
}

void loop() {

  
  if (! bmp.performReading()) {
    Serial.println("Failed to perform reading :(");
    return;
  }


  Serial.print("Temperature = ");
  Serial.print(bmp.temperature);
  Serial.println(" *C");

  Serial.print("Pressure = ");
  Serial.print(bmp.pressure / 100.0);
  Serial.println(" hPa");

  Serial.print("Approx. Altitude = ");
  Serial.print(bmp.readAltitude(SEALEVELPRESSURE_HPA));
  Serial.println(" m");

  Serial.println();
  delay(2000);

  
  // Conditional if: takes values given at startup and performs comparison on every sampling cycle. Turns given digital pin to high value and outputs console message to confirm. 
  // NOTE: Making a guess as to what sort of output the data is and assuming it is not typecast or anything in the background.
  // UPDATE: added bool state check which changes on end of startup and (hopefully) end of calibration sensing
   
  if (fireReady && bmp.readAltitude(SEALEVELPRESSURE_HPA) > 1000){
    digitalWrite(firingPin, HIGH);
    Serial.print('We have detonated at: ');
    Serial.print(bmp.readAltitude(SEALEVELPRESSURE_HPA));
    Serial.println('m. ;D');
  };

  
}
