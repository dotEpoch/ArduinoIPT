// Blinking LED with creative mathematical functions. Exercise 1.1.

int outPin = 7;

void setup() {
  // put your setup code here, to run once:
  pinMode(outPin, OUTPUT);

}

// 1. Random number generator for the delay arguments.
// Blinking of LED will be done with different randomly generated
// numbers in the loop function.

//void loop() {
  // put your main code here, to run repeatedly:
  //int randNumber1 = random(100,200);
  //int randNumber2 = random(10, 800);

  //digitalWrite(outPin, HIGH);
  //delay(randNumber1);
  //digitalWrite(outPin, LOW);
  //delay(randNumber2);

//}



// 2. Morse Code using an array object.
// Blinking of LED will be done by looping over an
// array with a set of numbers designed to replicate 
// S.O.S. morse code.


// int off = 200;
// int space = 1500;

// void loop() {
//   int myPins[] = {100, 100, 100, 500, 500, 500, 100, 100, 100};
//   for (byte i = 0; i < 9;  i = i + 1){
//     digitalWrite(outPin, HIGH);
//     delay(myPins[i]);
//     digitalWrite(outPin, LOW);
//     delay(off);
//   }
//   digitalWrite(outPin, LOW);
//   delay(space);


// }


// 3. Math functions.


void loop(){

  float time = 0;
  while (time <= 1000){
    time = time + 10;
    double y = sq(time);
    digitalWrite(outPin, HIGH);
    delay(y);
    digitalWrite(outPin, LOW);
    delay(100);
  }

}
