// adxl335 Config
const int powerpin = 58; // A4
const int groundpin = 54; // A0
const int xpin = A3;
int RawMin = 0;
int RawMax = 1023;
float xAccel = 0;
long xScaled = 0;
int xRaw = 0;
float prevAccel = 0;
const int sampleSize = 10;

// Microwave Sensor Config
#define ADCPin A1
#define printDelay 0 // ms to display result (0 = all results if possible)
#include "AnalogFrequency.h"

uint32_t displayTimer = 0;

// Ultrasonic Sensor Config
int trigPin = 12; // Trigger
int echoPin = 11; // Echo
long duration, cm, inches;

// Speaker Config
int Speaker = 3; // Speaker
int pauseBetweenNotes = 500;
int noteDuration = 200;
unsigned long previousMillis = 0;
boolean outputTone = false;

void setup() {
  // Serial Port Setup
  Serial.begin(115200);

  // adxl335 Setup
  pinMode(groundpin, OUTPUT);
  pinMode(powerpin, OUTPUT);
  digitalWrite(groundpin, LOW);
  digitalWrite(powerpin, HIGH);

  // Microwave Sensor Setup
  setupADC(ADCPin);

  //Ultrasonic Setup
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // adxl335
  xRaw = ReadAxis(xpin);
  xScaled = map(xRaw, RawMin, RawMax, -3000, 3000);
  prevAccel = xAccel;
  xAccel = xScaled / 1000.0;
  Serial.print("Raw: ");
  Serial.print(xRaw);
  Serial.print("\tAccel: ");
  Serial.print(xAccel);
  Serial.print("\t");
  float difference = xAccel - prevAccel;
  difference = abs(difference);
  if(difference > .5)
  {
    Serial.print("Heavy braking detected");
  }
  Serial.print("\n");
  delay(100);

  // Microwave Sensor
  if(fAvailable() && millis() - displayTimer > printDelay)
  {
    displayTimer = millis();
    uint32_t frequency = getFreq();
    float speedMPH = frequency / 31.36;
    if(speedMPH > 0.5)
    {
      Serial.print("Motion detected: ");
      Serial.print(speedMPH);
      Serial.println(" MPH");
    }
  }

  // Ultrasonic Sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);

}

//adxl335
int ReadAxis(int axisPin)
{
  long reading = 0;
  analogRead(axisPin);
  delay(1);
  for(int i = 0; i < sampleSize; i++)
  {
    reading += analogRead(axisPin);
  }
  return reading / SampleSize;
}
