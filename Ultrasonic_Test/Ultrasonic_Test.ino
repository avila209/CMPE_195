//Ultrasonic config
int trigPin = 12;    // Trigger
int echoPin = 11;    // Echo
long duration, cm, inches;

//Speaker config
int Speaker = 3;     // Speaker
int pauseBetweenNotes = 500;
int noteDuration = 200;
unsigned long previousMillis = 0;
boolean outputTone = false;
 
void setup() {
  //Serial Port begin
  Serial.begin (115200);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);

// Convert the time into a distance
  cm = (duration/2) / 29.1;     // Divide by 29.1 or multiply by 0.0343
  inches = (duration/2) / 74;   // Divide by 74 or multiply by 0.0135
  
  Serial.print(inches);
  Serial.print("in, ");
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();




  unsigned long currentMillis = millis();

  if(inches <= 54 && inches > 24){ //4.5 Feet, first tone
    pauseBetweenNotes = 750;
    
    if (outputTone) {
    // We are currently outputting a tone
    // Check if it's been long enough and turn off if so
        if (currentMillis - previousMillis >= noteDuration) {
            previousMillis = currentMillis;
            noTone(3);
            outputTone = false;
        }
    } else {
    // We are currently in a pause
    // Check if it's been long enough and turn on if so
        if (currentMillis - previousMillis >= pauseBetweenNotes) {
            previousMillis = currentMillis;
            tone(3, 350, 75);
            tone(3, 400, 75);
            tone(3, 450, 125);
            outputTone = true;
        }
    }

    Serial.print("First tone");
  }
  
  else if(inches <= 24 && inches > 12){ //2 Feet, second tone
    pauseBetweenNotes = 400;
    
    if (outputTone) {
    // We are currently outputting a tone
    // Check if it's been long enough and turn off if so
        if (currentMillis - previousMillis >= noteDuration) {
            previousMillis = currentMillis;
            noTone(3);
            outputTone = false;
        }
    } else {
    // We are currently in a pause
    // Check if it's been long enough and turn on if so
        if (currentMillis - previousMillis >= pauseBetweenNotes) {
            previousMillis = currentMillis;
            tone(3, 350, 50);
            tone(3, 400, 50);
            tone(3, 450, 100);
            outputTone = true;
        }
    }

    Serial.print("Second tone");
  }
  else if(inches <= 12 && inches > 0){ //1 Foot, final tone
    pauseBetweenNotes = 25;
    
    if (outputTone) {
    // We are currently outputting a tone
    // Check if it's been long enough and turn off if so
        if (currentMillis - previousMillis >= noteDuration) {
            previousMillis = currentMillis;
            noTone(3);
            outputTone = false;
        }
    } else {
    // We are currently in a pause
    // Check if it's been long enough and turn on if so
        if (currentMillis - previousMillis >= pauseBetweenNotes) {
            previousMillis = currentMillis;
            tone(3, 350, 25);
            tone(3, 400, 25);
            tone(3, 450, 75);
            outputTone = true;
        }
    }

    Serial.print("Third tone");
  }

  
  delay(250);
}
