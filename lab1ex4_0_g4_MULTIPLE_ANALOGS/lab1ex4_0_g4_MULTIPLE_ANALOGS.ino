

void setup() {
  // put your setup code here, to run once:
  pinMode(A5, INPUT);
  pinMode(A0, INPUT);
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);

}

void loop() {
  // put your main code here, to run repeatedly:

  Serial.print(analogRead(A0));
  Serial.print("\t");
  Serial.print(analogRead(A1));
  Serial.print("\t");
  Serial.print(analogRead(A2));
  Serial.print("\t");
  Serial.print(analogRead(A3));
  Serial.print("\t");
  Serial.print(analogRead(A4));
  Serial.print("\t");
  Serial.print(analogRead(A5));
  Serial.print("\t");
  Serial.println();
  delay(100);

}