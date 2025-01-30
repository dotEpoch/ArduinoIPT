int count = 0;

void setup() {
  // Establishes a connection to a serial port at 112500 baud
  Serial.begin(9600);

}

void loop() {
  Serial.print(count);
  Serial.print(":\t");
  Serial.println(millis());
  delay(1000);
  count++;

}
