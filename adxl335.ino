const int powerpin = 58;  //A4
const int groundpin = 54; //A0
const int xpin = A3;

int RawMin = 0;
int RawMax = 1023;

float xAccel = 0;
long xScaled = 0;
int xRaw = 0;

float prevAccel = 0;

const int sampleSize = 10;

void setup() {
  //analogReference(EXTERNAL);
  Serial.begin(9600);
  
  pinMode(groundpin, OUTPUT);
  pinMode(powerpin, OUTPUT);
  digitalWrite(groundpin, LOW);
  digitalWrite(powerpin, HIGH);
}

void loop() {
  xRaw = ReadAxis(xpin);

  xScaled = map(xRaw, RawMin, RawMax, -3000, 3000);
  
  prevAccel = xAccel;

  xAccel = xScaled / 1000.0;

  // put your main code here, to run repeatedly:
  Serial.print(xRaw);
  Serial.print("\t");
  Serial.print(xAccel);
  Serial.print("\t");

  float difference = xAccel - prevAccel;
  difference = abs(difference);
  if(difference > .5){
    Serial.print("Heavy braking detected");
    //Insert replay code with non interefering delays here



    
  }

  Serial.print("\n");
  // delay before next reading:
  delay(100);
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
