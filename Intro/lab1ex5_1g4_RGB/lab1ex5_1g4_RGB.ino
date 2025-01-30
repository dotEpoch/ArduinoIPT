void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);


  pinMode(A4, INPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int redMap = map(analogRead(A4), 0, 1023, 0, 128) ;
  int greenMap = map(analogRead(A4), 0, 1023, 0, 255);
  int bluMap = map(analogRead(A4), 0, 1023, 0, 128);
  Serial.print(redMap);
  Serial.print("\t");
  Serial.print(greenMap);
  Serial.print("\t");
  Serial.print(bluMap);
  Serial.println();
  
  
  analogWrite(11, greenMap); //Red
  analogWrite(10, redMap); //Green
  analogWrite(9, bluMap); //Blue

}

