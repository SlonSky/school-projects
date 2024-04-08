#include <Arduino.h>
#include <SoftwareSerial.h>

SoftwareSerial Bluetooth(0, 1);

const int pin34 = 4;
bool newline_printed = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Arduino is ready");
 
  Bluetooth.begin(9600);  
  Serial.println("Bluetooth is ready");

  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
 if(Bluetooth.available())
  { 
    digitalWrite(8, HIGH); 
    char c = Bluetooth.read();
    if(c == '#')
    {
      if(!newline_printed)
      {
        Serial.println("");
        newline_printed = true;
      }
    }
    else
    {
      Serial.print(c);
      newline_printed = false;
    }
    
    digitalWrite(8, LOW);
  }
 
if(Serial.available())
  {
   
    digitalWrite(7, HIGH);  
    char c = Serial.read();
    Bluetooth.print(c);
    
    digitalWrite(7, LOW);  
  }
}
