// Code that enables a blinking LED light.
// In the first lines 6-7, we define integer values
// for the pin number, how long we want the LED to 
// be on or off in miliseconds.
// In the setup, we specify that the pin chosen will act
// as an output.
// In the loop, we first assign the pin to be HIGH, meaning
// it will provide current. This happens for delay(on) amount 
// of time where the delay( ) function stops program for that
// amount of time.
// After, the program moves on and sets the pin to LOW which makes 
// it a ground, and due to the unidirectional design of the LED,
// the light turns off and with delay(off) we specify how long we 
// would like this program to be off. It then loops everything.




// Global variables declared before the setup function:
int outPin = 7; // Specify the output pin.
int on = 200; // Specify the amount of time LED is on in miliseconds.
int off = 500; // Specify the amount of time LED is off in miliseconds.


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
