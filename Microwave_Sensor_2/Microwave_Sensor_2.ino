#define SENSITIVITY 7

// The analog pin to use
#define ADCPin A6

// Incoming data is summed, so fetching the results every second
// will indicate speed over the previous second
// How often in mS to display the results ( 0 = print all results if possible)
#define printDelay 0

//*****************************************/

#include "AnalogFrequency.h"

const int digitalPin = 4;

uint32_t displayTimer = 0;

void setup() {
  Serial.begin(115200);
  setupADC(ADCPin);
  pinMode(digitalPin, OUTPUT);
  digitalWrite(digitalPin, LOW);
}

void loop() {

 if( fAvailable() && millis() - displayTimer > printDelay ){
   displayTimer = millis();   
   uint32_t frequency = getFreq();
   float speedMPH = frequency/31.36;
   if(speedMPH > 1 && speedMPH < 20){
      Serial.print("Blindspot on");
      Serial.print("  MPH ");
      Serial.println(speedMPH);
      digitalWrite(digitalPin, HIGH);
   }
   else {
      digitalWrite(digitalPin, LOW);
   }
 }
}

//https://github.com/TMRh20/AnalogFrequency
