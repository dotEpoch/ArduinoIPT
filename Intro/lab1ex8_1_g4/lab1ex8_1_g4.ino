void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT);
  attachInterrupt(digitalPinToInterrupt(2), loop, HIGH);
  
  analogWrite(A0, OUTPUT);
  analogWrite(A1, OUTPUT);
  analogWrite(A2, OUTPUT);

  Serial.begin(115200);
}


void loop() {
  // put your main code here, to run repeatedly:
  static int count = 0;
  static bool pressed = false;
  
  if (digitalRead(2) == HIGH) {
    if (pressed == false) {
      count++ % 3;
      pressed = true;
      Serial.println(count);
    }

    //while (digitalRead(2) == HIGH) delay(10);
  }
  else {
    pressed = false;

  }
  
  analogWrite(A0, 255);
  analogWrite(A1, 255);
  analogWrite(A2, 255);

  Serial.print("Number of button presses: \t");
  Serial.println(count);
  
}