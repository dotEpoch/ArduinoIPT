void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

}

int multiplyMyfunction(int x, int y){
  int result;

  result = x * y;
  return result;
}

void loop() {
  // put your main code here, to run repeatedly:
  int i = 2;
  int j = 3;
  int k;

  k = multiplyMyfunction(i, j);
  Serial.println(k);
  delay(500);

}
