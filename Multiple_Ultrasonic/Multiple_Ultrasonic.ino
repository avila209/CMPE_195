#include <NewTone.h>
#include <NewPing.h>

//Ultrasonic config
int trigPin_1 = 13;    // Trigger
int echoPin_1 = 12;    // Echo
int trigPin_2 = 11;    // Trigger
int echoPin_2 = 10;    // Echo
int trigPin_3 = 9;    // Trigger
int echoPin_3 = 8;    // Echo
int trigPin_4 = 7;    // Trigger
int echoPin_4 = 6;    // Echo

int MAX_DISTANCE = 500;

long duration, cm, inches;

long duration_1, duration_2, duration_3, duration_4;
long cm_1, cm_2, cm_3, cm_4, inches_1, inches_2, inches_3, inches_4;

  int previous_1 = 999;
  int previous_2 = 999;
  int previous_3 = 999;
  int previous_4 = 999;

NewPing Sensor1(trigPin_1, echoPin_1, MAX_DISTANCE);
NewPing Sensor2(trigPin_2, echoPin_2, MAX_DISTANCE);
NewPing Sensor3(trigPin_3, echoPin_3, MAX_DISTANCE);
NewPing Sensor4(trigPin_4, echoPin_4, MAX_DISTANCE);

//Speaker config
int Speaker = 3;     // Speaker
int pauseBetweenNotes = 500;
int noteDuration = 200;
unsigned long previousMillis = 0;
boolean outputTone = false;


//Accelerometer config
const int powerpin = 58;    //A4
const int groundpin = 54;   //A0
const int xpin = A3;
const int accelOutputPin = A8;
uint8_t pinMask = 0;        // Pin bitmask
volatile uint8_t *pinOutput // Output port register
unsigned long previousAccelMillis = 0;

int hardBrakeDelay = 250;

int RawMin = 0;
int RawMax = 1023;

float xAccel = 0;
long xScaled = 0;
int xRaw = 0;

float prevAccel = 0;

const int sampleSize = 10;



void setup() {
  //Serial Port begin
  Serial.begin (115200);

  //Accelerometer
  pinMode(groundpin, OUTPUT);
  pinMode(powerpin, OUTPUT);
  pinMode(accelOutputPin, OUTPUT);
  digitalWrite(groundpin, LOW);
  digitalWrite(powerpin, HIGH);
  digitalWrite(accelOutputPin, HIGH);
}

bool first_round = true;

void loop() {
  
  delay(10);

  duration_1 = Sensor1.ping();
  duration_2 = Sensor2.ping();
  duration_3 = Sensor3.ping();
  duration_4 = Sensor4.ping();

  // Convert the time into a distance
  cm_1 = (duration_1 / 2) / 29.1;   // Divide by 29.1 or multiply by 0.0343
  inches_1 = (duration_1 / 2) / 74; // Divide by 74 or multiply by 0.0135

  cm_2 = (duration_2 / 2) / 29.1;   // Divide by 29.1 or multiply by 0.0343
  inches_2 = (duration_2 / 2) / 74; // Divide by 74 or multiply by 0.0135

  cm_3 = (duration_3 / 2) / 29.1;   // Divide by 29.1 or multiply by 0.0343
  inches_3 = (duration_3 / 2) / 74; // Divide by 74 or multiply by 0.0135

  cm_4 = (duration_4 / 2) / 29.1;   // Divide by 29.1 or multiply by 0.0343
  inches_4 = (duration_4 / 2) / 74; // Divide by 74 or multiply by 0.0135

  if(first_round) inches_1 = 999;
  else if(inches_1 == 0 && inches_1 != 999) inches_1 = previous_1; 
  else if(inches_1 != 0) previous_1 = inches_1;

  if(first_round) inches_2 = 999;
  else if(inches_2 == 0 && inches_2 != 999) inches_2 = previous_2; 
  else if(inches_2 != 0) previous_2 = inches_2;

  if(first_round) inches_3 = 999;
  else if(inches_3 == 0 && inches_3 != 999) inches_3 = previous_3; 
  else if(inches_3 != 0) previous_3 = inches_3;

  if(first_round) inches_4 = 999;
  else if(inches_4 == 0 && inches_4 != 999) inches_4 = previous_4; 
  else if(inches_4 != 0) previous_4 = inches_4;

  Serial.print("Sensor 1: ");
  Serial.print(inches_1);
  Serial.print("in, ");
  Serial.print(cm_1);
  Serial.print("cm \t");

  Serial.print("Sensor 2: ");
  Serial.print(inches_2);
  Serial.print("in, ");
  Serial.print(cm_2);
  Serial.print("cm \t");

  Serial.print("Sensor 3: ");
  Serial.print(inches_3);
  Serial.print("in, ");
  Serial.print(cm_3);
  Serial.print("cm \t");

  Serial.print("Sensor 4: ");
  Serial.print(inches_4);
  Serial.print("in, ");
  Serial.print(cm_4);
  Serial.print("cm");
  Serial.println();
  
  int min_1 = min(inches_1, inches_2);
  int min_2 = min(inches_3, inches_4);
  int minimum = min(min_1, min_2);

  first_round = false;
  
  unsigned long currentMillis = millis();

  if(minimum <= 54 && minimum > 24){ //4.5 Feet, first tone
      pauseBetweenNotes = 750;
  
      if (outputTone) {
      // We are currently outputting a tone
      // Check if it's been long enough and turn off if so
          if (currentMillis - previousMillis >= noteDuration) {
              previousMillis = currentMillis;
              noNewTone(3);
              outputTone = false;
          }
      } else {
      // We are currently in a pause
      // Check if it's been long enough and turn on if so
          if (currentMillis - previousMillis >= pauseBetweenNotes) {
              previousMillis = currentMillis;
              NewTone(3, 350, 75);
              NewTone(3, 400, 75);
              NewTone(3, 450, 125);
              outputTone = true;
          }
      }
  
      Serial.print("First tone");
  }

  else if(minimum <= 24 && minimum > 12){ //2 Feet, second tone
      pauseBetweenNotes = 400;
  
      if (outputTone) {
      // We are currently outputting a tone
      // Check if it's been long enough and turn off if so
          if (currentMillis - previousMillis >= noteDuration) {
              previousMillis = currentMillis;
              noNewTone(3);
              outputTone = false;
          }
      } else {
      // We are currently in a pause
      // Check if it's been long enough and turn on if so
          if (currentMillis - previousMillis >= pauseBetweenNotes) {
              previousMillis = currentMillis;
              NewTone(3, 350, 50);
              NewTone(3, 400, 50);
              NewTone(3, 450, 100);
              outputTone = true;
          }
      }
  
      Serial.print("Second tone");
  }

  else if(minimum <= 12 && minimum > 0){ //1 Foot, final tone
      pauseBetweenNotes = 25;
  
      if (outputTone) {
      // We are currently outputting a tone
      // Check if it's been long enough and turn off if so
          if (currentMillis - previousMillis >= noteDuration) {
              previousMillis = currentMillis;
              noNewTone(3);
              outputTone = false;
          }
      } else {
      // We are currently in a pause
      // Check if it's been long enough and turn on if so
          if (currentMillis - previousMillis >= pauseBetweenNotes) {
              previousMillis = currentMillis;
              NewTone(3, 350, 25);
              NewTone(3, 400, 25);
              NewTone(3, 450, 75);
              outputTone = true;
          }
      }
  
      Serial.print("Third tone");
  }


  //Acelerometer Code:
  unsigned long currentAccelMillis = millis();
  xRaw = ReadAxis(xpin);
  xScaled = map(xRaw, RawMin, RawMax, -3000, 3000);
  prevAccel = xAccel;
  xAccel = xScaled / 1000.0;

  Serial.print("Acelerometer Data: ");
  Serial.print(xRaw);
  Serial.print("\t");
  Serial.print(xAccel);
  Serial.print("\t");

  float difference = xAccel - prevAccel;
  difference = abs(difference);
  if(difference > .75){
    Serial.print("Heavy braking detected");
    if(currentAccelMillis - previousAccelMillis >= hardBrakeDelay) {
      digitalWrite(accelOutputPin, LOW);
      digitalWrite(accelOutputPin, HIGH);
      digitalWrite(accelOutputPin, LOW);
      digitalWrite(accelOutputPin, HIGH);
      digitalWrite(accelOutputPin, LOW);
      digitalWrite(accelOutputPin, HIGH);
      digitalWrite(accelOutputPin, LOW);
      digitalWrite(accelOutputPin, HIGH);
      digitalWrite(accelOutputPin, LOW);
      digitalWrite(accelOutputPin, HIGH);
      digitalWrite(accelOutputPin, LOW);
      digitalWrite(accelOutputPin, HIGH);
      digitalWrite(accelOutputPin, LOW);
      digitalWrite(accelOutputPin, HIGH);
      digitalWrite(accelOutputPin, LOW);
      digitalWrite(accelOutputPin, HIGH);
    }
  } else {
    // Default, no breaking or too light of a brake
    digitalWrite(accelOutputPin, HIGH);
  }

  Serial.print("\n");

  delay(10);
}


int ReadAxis(int axisPin){
  long reading = 0;
  analogRead(axisPin);
  delay(1);
  for(int i = 0; i < sampleSize; i++){
    reading += analogRead(axisPin);
  }
  return reading/sampleSize;
}
