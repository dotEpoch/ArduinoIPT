// code for use with  StepperOnilne DM320T controller

int inPin = A0;
int supplyPin = 13;
int dirPin = 9;
int pulPin = 8;
// minimum direction change delay is 8 microseconds for DMT320T
int dirDelay = 10;
// minimum pulse length is 8 microseconds for DM320T
int pulDelay = 10;
long rpsMicro = 0;

boolean dirLow = true;

int getMax(int* array, int size){
int maxIndex = 0;
 int max = array[maxIndex];
 for (int i=1; i<size; i++){
   if (max<array[i]){
     maxIndex = i;
     max = array[i];
   }
 }
 return maxIndex;
}

int getMin(int* array, int size){
int minIndex = 0;
 int min = array[minIndex];
 for (int i=1; i<size; i++){
   if (min>array[i]){
     minIndex = i;
     min = array[i];
   }
 }
 return minIndex;
}

void setup() {
  pinMode(supplyPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(pulPin, OUTPUT);
  pinMode(inPin, INPUT);

  digitalWrite(supplyPin,HIGH);
  digitalWrite(dirPin, LOW);

  Serial.begin(115200);
  Serial.println("<laserLab.ino>\n");
  
  float rpm = 33.0;
  float rps = rpm/60.0;

  //if rpsMicro > ~16000, havoc! provide for this.
  rpsMicro = (1000000.0/(rps * 400.0))/2.0 - pulDelay;
  delay(1000);

  int pinArray[200];
  Serial.println("Driving motor...");
  for(int i = 0; i < 200; i++){
    step();
    pinArray[i] = analogRead(inPin);
  }

  //int maxPinIndex = getMax(pinArray, 200);
  int minPinIndex = getMin(pinArray, 200);

  delay(500);
  changeDir();

  Serial.println("Reversing...");
  for(int i = 0; i < (200 - minPinIndex); i++){
    step();
    
  }

  Serial.println("Input a number of steps to turn, negative to reverse:");
}

void changeDir(){
  dirLow = !dirLow;
  if(dirLow) digitalWrite(dirPin, LOW);
  else digitalWrite(dirPin, HIGH);
  delayMicroseconds(rpsMicro);
  delayMicroseconds(dirDelay);
}

void step(){
  digitalWrite(pulPin, LOW);
  delayMicroseconds(rpsMicro);
  delayMicroseconds(pulDelay);
  digitalWrite(pulPin, HIGH);
  delayMicroseconds(rpsMicro);
  delayMicroseconds(pulDelay);
}

void loop() {
  if(Serial.available()){
    int stepInput = Serial.parseInt();
    if(stepInput < 0) digitalWrite(dirPin, LOW);
    else digitalWrite(dirPin, HIGH);
    delayMicroseconds(dirDelay);
    stepInput = abs(stepInput);
    for(int i = 0; i < stepInput; i++){
      step();
      //Serial.print("PD Analog read: ");
      Serial.print(analogRead(inPin));
      Serial.print(',');
    }
    Serial.println();
    stepInput = 0;
  }
}


