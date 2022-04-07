#include <Servo.h>

int delaytime = 25;

Servo servo5;
int q5min = 0;    //手先を閉じた状態
int q5max = 180;  //壁に接触

void setup() {
    Serial.begin(9600);
    Serial.println("Hello Arduino!");

    servo5.attach(9);
    servo5.write(q5min);
    delay(delaytime);
}

void loop() {
    for (int i = q5min; i <= q5max; i++) {
        servo5.write(i);
        Serial.println(i);
        delay(delaytime);
    }
    for (int i = q5max; i >= q5min; i--) {
        servo5.write(i);
        Serial.println(i);
        delay(delaytime);
    }
}
