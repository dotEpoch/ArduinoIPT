void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(11, OUTPUT);

}

float TriangleWave(float t, float p){
  float result;

  result = 2. * abs(t/p - floor( (t/p) + (1./2.)) );
  return result;
}

void loop() {
  // put your main code here, to run repeatedly:
  float P = 2.;
  static float T;
  float k;

  T = T + 0.0001;

  k = TriangleWave(T, P);
  Serial.println(k);
  //delay(50);
  analogWrite(11, 255*k);


}
