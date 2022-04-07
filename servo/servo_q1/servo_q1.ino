#include <Servo.h>

int delaytime = 25;

Servo servo1;
int q1min = 0;    //手先を閉じた状態
int q1max = 146;  //壁に接触

void setup() {
    Serial.begin(9600);
    Serial.println("Hello Arduino!");

    servo1.attach(9);
    servo1.write(q1min);
    delay(delaytime);
}

void loop() {
    for (int i = q1min; i <= q1max; i++) {
        servo1.write(i);
        Serial.println(i);
        delay(delaytime);
    }
    for (int i = q1max; i >= q1min; i--) {
        servo1.write(i);
        Serial.println(i);
        delay(delaytime);
    }
}
