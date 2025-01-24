void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT);
  //pinMode(2, INPUT_PULLUP);

  Serial.begin(115200);

}


void loop() {
  // put your main code here, to run repeatedly:
  static int count = 0;
  static bool pressed = false;
  
  if (digitalRead(2) == HIGH) {
    if (pressed == false) {
      count++;
      pressed = true;
      Serial.print("Number of button presses: \t");
      Serial.println(count);
    }

    //while (digitalRead(2) == HIGH) delay(10);
  }
  else {
    pressed = false;
  }
  

  delay(100);
}
