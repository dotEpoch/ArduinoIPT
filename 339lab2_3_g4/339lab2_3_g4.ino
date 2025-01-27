bool newData = false;
unsigned long startMillis;
unsigned long time;
char receivedChar;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  //startMillis = millis(); // initial start time

  //Pins
  pinMode(2, INPUT);
  pinMode(A5, INPUT);
  pinMode(5, OUTPUT);
  digitalWrite(5, HIGH);
  

  //Interrupts
  attachInterrupt(digitalPinToInterrupt(2), loop, HIGH);

}

void loop() {
  //buttonPress();
  
  static int count = 0;
  static bool pressed = false;
  
  if (digitalRead(2) == HIGH) {
    if (pressed == false) {
      pressed = true;

      count++;
      float voltage = float(analogRead(A5))/1024 * 5.00;
      time = millis()/1000.00;

      //Serial.print("<");
      Serial.print(count);
      Serial.print(",");
      Serial.print(voltage);
      Serial.print(",");
      Serial.print(time);
      Serial.print("\n");

    }
  }
  else {
    pressed = false;

  }
  delay(1000);
  //Serial.print("Number of button presses: \t");
  //Serial.println(count);

}

/*void buttonPress(){

  if (digitalRead(2) == HIGH) {
    if (pressed == false) {
      pressed = true;

      count++;
      float voltage = map(analogRead(A5), 0, 1023, 0, 5.0);
      time = millis();

      Serial.print(count);
      Serial.print(",");
      Serial.print(voltage);
      Serial.print(",");
      Serial.print(time);
      Serial.print(",");
      Serial.println();

    }
  }
  else {
    pressed = false;
  }
}*/