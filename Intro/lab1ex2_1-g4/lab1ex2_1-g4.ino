int outPin = 7; // Specify the output pin.
int on = 20; // Specify the amount of time LED is on in miliseconds.
int off = 20; // Specify the amount of time LED is off in miliseconds


// Code here runs for the first time in the program.
void setup() {
  // put your setup code here, to run once:
  pinMode(outPin, OUTPUT);

}


// Code here runs in an endless loop.
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(outPin, HIGH); //
  delay(on);
  digitalWrite(outPin, LOW);
  delay(off);
}

