#include <Servo.h>

Servo rightServo, leftServo;

int rightPort = 11, leftPort = 10;
int rightSignal = 90, leftSignal = 90;
String income, left, right;

void setup() {
  Serial.begin(9600);
  rightServo.attach(rightPort);
  leftServo.attach(leftPort);
}

void loop() {
  if(Serial.available() > 0){
    income = Serial.readString();
    right = income.substring(0, 3);
    left = income.substring(3, 6);
    rightSignal = right.toInt();
    leftSignal = left.toInt();
  }
  rightServo.write(rightSignal);
  leftServo.write(leftSignal);
}

