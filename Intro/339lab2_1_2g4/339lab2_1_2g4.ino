bool newData = false;

char receivedChar;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  recvOneChar();

  

  if(newData){

    if(receivedChar == 't') {
      //transmmit
      //Serial.print(Serial.availableForWrite());
      Serial.print("text,42,3.14159,");
    }
    newData = false;
  }

}

void recvOneChar(){
  if(Serial.available() > 0) {
    receivedChar = Serial.read();
    newData = true;
  }
}