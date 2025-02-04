const int geigerPin = 2;
volatile int count = 0;
unsigned long previousMillis = 0;

void timePulse() {
  unsigned long currentMillis = millis();

  Serial.print(currentMillis - previousMillis);
  Serial.print(",");
  previousMillis = currentMillis;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(geigerPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(geigerPin), timePulse, RISING);
}

void loop() {
  delay(1000)

}
