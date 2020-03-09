#define SENSITIVITY 7

// The analog pin to use
#define ADCPin A1

// Incoming data is summed, so fetching the results every second
// will indicate speed over the previous second
// How often in mS to display the results ( 0 = print all results if possible)
#define printDelay 0

//*****************************************/

#include "AnalogFrequency.h"

uint32_t displayTimer = 0;
bool detection;

void setup() {
  Serial.begin(115200);
  setupADC(ADCPin);
}

void loop() {

 if( fAvailable() && millis() - displayTimer > printDelay ){
   displayTimer = millis();   
   uint32_t frequency = getFreq();
   float speedMPH = frequency/31.36;
   if(speedMPH > 1 && speedMPH < 20){
      detection = true;
      Serial.print("Blindspot on");
      Serial.print("  MPH ");
      Serial.println(speedMPH);
      Serial.write(detection);
   }
   else {
      detection = false;
      Serial.write(detection);
   }
 }
}

//https://github.com/TMRh20/AnalogFrequency
