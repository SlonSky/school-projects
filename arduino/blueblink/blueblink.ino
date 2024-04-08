#include <SoftwareSerial.h>

SoftwareSerial bluetooth(0,1);

void setup() {
  // put your setup code here, to run once:
  bluetooth.begin(9600);
  Serial.begin(9600);
  
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  
  digitalWrite(10, HIGH);
  delay(1000);
  digitalWrite(10, LOW);  
  bluetooth.write("AT+VERSION\r\n");
  
}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(9, HIGH);
      delay(100);
      digitalWrite(9, LOW); 
  if(bluetooth.available()) {
    char num = bluetooth.read();
    Serial.println(num);
    int n = (int)(num - '0');
    if(n >= 0 && n <= 9) {
          
    
    for(int i = 0; i < n; i++){
      digitalWrite(10, HIGH);
      delay(400);
      digitalWrite(10, LOW);          
    }
    
    }  
  }
}
