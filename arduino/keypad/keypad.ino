#include <Keypad.h>

const byte ROWS = 4;
const byte COLUMNS = 4;
char keys[ROWS][COLUMNS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {11, 10, 9, 8};
byte columnPins[COLUMNS] = {7, 6, 5, 4};

int del = 1000;
int sound = 2;
Keypad keypad = Keypad(makeKeymap(keys), rowPins, columnPins, ROWS, COLUMNS);
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(sound, OUTPUT);
//  pinMode(3, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  // digitalWrite(2, HIGH);
  // digitalWrite(2, LOW);
  // delay(2000)
  char key = keypad.getKey();
  if(key) {
    Serial.println(key);
    tone(sound, (int)key*50, 300);
  }
  
  
}
