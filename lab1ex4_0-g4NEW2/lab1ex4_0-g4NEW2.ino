void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  float size = (1024 - analogRead(A0))/14;
  Serial.print("[");
  //int length = 1/size * 72;
  float voltage = float(analogRead(A0))/1024 * 5.00;


  String voltString = "thisIsACharacterStringWhoseLengthRepresentsAMeasuredAnalogVoltageOnPinA0";

  for (int i = 0; i<size-1; i++) {
    Serial.print(voltString[i]);
  }

  //String output = "] ---> Current Voltage" + "V"
  Serial.println("]");

  delay(100);

}