void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
  digitalWrite(11, HIGH);

  pinMode(A0, INPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(analogRead(A0)/4);
  analogWrite(11, analogRead(A0)/4);

}
