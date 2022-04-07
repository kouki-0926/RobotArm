#include <Servo.h>

int delaytime = 25;

Servo servo4;
int q4min = 0;    //手先を閉じた状態
int q4max = 180;  //壁に接触

void setup() {
    Serial.begin(9600);
    Serial.println("Hello Arduino!");

    servo4.attach(9);
    servo4.write(q4min);
    delay(delaytime);
}

void loop() {
    for (int i = q4min; i <= q4max; i++) {
        servo4.write(i);
        Serial.println(i);
        delay(delaytime);
    }
    for (int i = q4max; i >= q4min; i--) {
        servo4.write(i);
        Serial.println(i);
        delay(delaytime);
    }
}
