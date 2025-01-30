//Vincent Aucoin, Didar Sedghi

//global constants
int outPin = 7;
int on = 0;
int off = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(outPin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(outPin, HIGH);
  delayMicroseconds(on);
  digitalWrite(outPin,LOW);
  delayMicroseconds(off);
}
