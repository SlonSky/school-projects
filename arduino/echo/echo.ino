#include <NewPing.h>

int trig_pin = 4;
int echo_pin = 5;
int max_distance = 200;

NewPing sonar(trig_pin, echo_pin, max_distance);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
//  pinMode(trig_pin, OUTPUT);
//  pinMode(echo_pin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
//  digitalWrite(trig_pin, LOW);
//  delayMicroseconds(5);
//  digitalWrite(trig_pin, HIGH);
//  delayMicroseconds(10);
//  digitalWrite(trig_pin, LOW);
//
//  pinMode(echo_pin, INPUT);
//  duration = pulseIn(echo_pin, HIGH);
//
//  cm = (duration / 2) / 29.1;
//  inches = (duration / 2) / 74;
//
//  Serial.print(inches);
//  Serial.print("in, ");
//  Serial.print(cm);
//  Serial.print("cm");
//  Serial.println();
//  
//  delay(250);

  delay(50);
  unsigned int uS = sonar.ping_cm();
  Serial.println(uS);
}
