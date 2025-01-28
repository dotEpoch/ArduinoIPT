/*
Authors:
  Vincent Aucoin [261055005]
  Didar Sedghi [261002363]
Date:
  2025-01-21
Rights:
  Copy of 'receiveAsingleCharacter.ino' by Robert Turner.
*/


//-------------- Instructions ----------------\\ 

/*
Control an RGB LED with Serial input commands.

We use the following pin assignments:
  pin 9 - red,
  pin 10 - green,
  pin 11 - blue. 

Arduino Read:

Arduino Write:
*/



//-------------- Initialization --------------\\ 
// Pins connected to LEDs
int ledPin[] = {9, 10, 11};
// New serial data flag
bool newData = false;
// Data character
char receivedChar;



//----------------- Functions ----------------//
void setup() {
  // Start Serial COM with a baudrate of 115200
  Serial.begin(115200);

  // Set all LED pins to OUTPUT mode
  int ledPinLength = sizeof(ledPin)/sizeof(int);
  for(int i = 0; i < ledPinLength; i++) pinMode(ledPin[i], OUTPUT);
}


void recvOneChar(){
  if (Serial.available() > 0) {
    receivedChar = Serial.read();
    newData = true;
  }
}


void lightLED(){
  if (newData == true) {
    if (receivedChar == 'r') {
      digitalWrite(ledPin[0], HIGH);
      digitalWrite(ledPin[1], LOW);
      digitalWrite(ledPin[2], LOW);
    }
    else if (receivedChar == 'g') {
      digitalWrite(ledPin[0], LOW);
      digitalWrite(ledPin[1], HIGH);
      digitalWrite(ledPin[2], LOW);
    }
    else if (receivedChar == 'b') {
      digitalWrite(ledPin[0], LOW);
      digitalWrite(ledPin[1], LOW);
      digitalWrite(ledPin[2], HIGH);
    }
    newData = false;
  }
}



//----------------- Main Loop ----------------//
void loop() {
  // Attempt to retreive a character from the Serial line
  recvOneChar();
  // Change LED output according to new Serial data
  lightLED();

}
