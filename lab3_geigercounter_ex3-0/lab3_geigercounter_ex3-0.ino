const int geigerPin = 2;
volatile int count = 0;
const unsigned long interval = 2000;
unsigned long previousMillis = 0;

void countPulse() {
  count++;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(geigerPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(geigerPin), countPulse, RISING);
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval){
    Serial.print("Counts in last ");
    Serial.print(interval / 1000.0);
    Serial.print(" seconds: ");
    Serial.println(count);

    count = 0; // Reset count
    previousMillis = currentMillis;
  }

}
