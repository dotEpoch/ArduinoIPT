//Vincent Aucoin, Didar Sedghi

//global constants
int outPin = 7;
int delayQuick = 100;


void setup() {
  // put your setup code here, to run once:
  pinMode(outPin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  
  
    digitalWrite(outPin, HIGH);
    delay(delayQuick);
    delayQuick = delayQuick - 5;
    digitalWrite(outPin, LOW);
    delay(delayQuick);

    if (delayQuick <= 10) delayQuick = 200;
}
