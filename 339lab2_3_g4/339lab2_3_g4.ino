bool newData = false;

char receivedChar;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  //Pins
  pinMode(6, INPUT);
  pinMode(A5, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  static int count = 0;
  static bool pressed = false;
  static int time = 0;
  //buttonPress();
  
  if (digitalRead(6) == HIGH) {
    if (pressed == false) {
      pressed = true;

      count++;
      float voltage = range(analogRead(A5), 0, 1023, 0, 5.0);

      Serial.print(count);
      Serial.print(",");
      Serial.print(voltage);
      Serial.print(",");
      Serial.print(time);
      Serial.print(",");
      



    }

    //while (digitalRead(2) == HIGH) delay(10);
  }
  else {
    pressed = false;
  }

  delay(1000)
  time++;

}

//void buttonPress(){

//}