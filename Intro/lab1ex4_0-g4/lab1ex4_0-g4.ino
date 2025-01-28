void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  Serial.begin(115200);
  pinMode(A2, OUTPUT); //output pin

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(A2, HIGH);
  delay(10);
  //digitalWrite(A5, LOW);
  //delay(10);
  Serial.println(analogRead(A0));
  delay(100);

}
