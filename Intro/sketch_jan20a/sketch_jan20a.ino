void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  //INPUTS
  pinMode(2, INPUT);
  //OUTPUTS
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);


}

float TriangleWave(float t, float p){
  float result;

  result = 2. * abs(t/p - floor( (t/p) + (1./2.)) );
  return result;
}



void loop() {
  // --- Intensity Fluctuation ---
  float P = 2.;
  static float T;
  float k;

  T = T + 0.0001;

  k = TriangleWave(T, P);
  //Serial.println(k);



  // --- Color Choice ---
  static int count = 0;
  static int color = 0;
  static bool pressed = false;

  if (digitalRead(2) == HIGH) {
    if (pressed == false) {
      count++;
      color = count % 3;
      pressed = true;
      
      Serial.print("Current color is: ");
      Serial.println(color);
    }

  }
  else {
    pressed = false;
  }

  //int colorMap = map(k, 0, 1, 0, 255);
  float colorMap = k * 255;
  switch (color) {
    case 0:
      analogWrite(11, colorMap);
      //off
      analogWrite(10, 0);
      analogWrite(9, 0);
      break;

    case 1:
      analogWrite(10, colorMap);
      //off
      analogWrite(11, 0);
      analogWrite(9, 0);
      break;

    case 2:
      analogWrite(9, colorMap);
      //off
      analogWrite(11, 0);
      analogWrite(10, 0);
      break;
  }
  


}