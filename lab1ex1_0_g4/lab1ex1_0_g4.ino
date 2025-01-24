//Vincent Aucoin, Didar Sedghi

//global constants
int outPin = 7;
int on = 200;
int off = 500;

void setup() {
  // put your setup code here, to run once:
  pinMode(outPin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(outPin, HIGH);
  delay(on);
  digitalWrite(outPin,LOW);
  delay(off);
}
