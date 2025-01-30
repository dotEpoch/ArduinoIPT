
void setup() {
  Serial.begin(115200);

  //Pins
  pinMode(2, INPUT);
  
  //Interrupts
  attachInterrupt(digitalPinToInterrupt(2), geigerClick, HIGH);
}

unsigned long time;
float interval = 1000.0;

void loop() {
  static int count = 0;

  geigerClick(count)
  time = millis();

}

int geigerClick(count){
  static bool pressed = false;

  if (digitalRead(2) == HIGH) {
    if (pressed == false) {
      pressed = true;
      count++;

      Serial.print(count);
    }
  }
  else {
    pressed = false;
  }

}