//Accelerometer config
const int powerpin = 58;  //A4
const int groundpin = 54; //A0
const int xpin = A3;
const int accelOutputPin = A8;
uint8_t pinMask = 0;         // Pin bitmask.
volatile uint8_t *pinOutput; // Output port register
unsigned long previousAccelMillis = 0;

//int lightBrakeDelay = 1000;
//int mediumBrakeDelay = 500;
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

void loop() {
  // put your main code here, to run repeatedly:
  
  unsigned long currentAccelMillis = millis();
    //Acelerometer Code:
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
  /*if(difference > .25){
    Serial.print("Light braking detected");
    if(currentAccelMillis - previousAccelMillis >= lightBrakeDelay) {
      previousAccelMillis = currentAccelMillis;
      digitalWrite(accelOutputPin, !digitalRead(accelOutputPin));
    }
  } else if (difference > .5) {
    Serial.print("Medium braking detected");
    if(currentAccelMillis - previousAccelMillis >= mediumBrakeDelay) {
      previousAccelMillis = currentAccelMillis;
      digitalWrite(accelOutputPin, !digitalRead(accelOutputPin));
    }
  } else*/ 
  if (difference > .75) {
    Serial.print("Heavy braking detected");
    if(currentAccelMillis - previousAccelMillis >= hardBrakeDelay) {
      previousAccelMillis = currentAccelMillis;
      digitalWrite(accelOutputPin, !digitalRead(accelOutputPin));
      digitalWrite(accelOutputPin, !digitalRead(accelOutputPin));
      digitalWrite(accelOutputPin, !digitalRead(accelOutputPin));
      digitalWrite(accelOutputPin, !digitalRead(accelOutputPin));
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
