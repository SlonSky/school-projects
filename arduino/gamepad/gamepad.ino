#include <SoftwareSerial.h>

SoftwareSerial bluetooth(0, 1);

void setup() {
  // put your setup code here, to run once:
  bluetooth.begin(9600);
  
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
}
