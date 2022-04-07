#include <Servo.h>

int delaytime = 25;

Servo servo6;
int q6min = 0;   //手先を開けた状態
int q6max = 75;  //手先を閉じた状態

void setup() {
    Serial.begin(9600);
    Serial.println("Hello Arduino!");

    servo6.attach(9);
    servo6.write(q6max);
    delay(delaytime);
}

void loop() {
    for (int i = q6max; i >= q6min; i--) {
        servo6.write(i);
        Serial.println(i);
        delay(delaytime);
    }
    for (int i = q6min; i <= q6max; i++) {
        servo6.write(i);
        Serial.println(i);
        delay(delaytime);
    }
}
