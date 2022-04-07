#include <Servo.h>

int delaytime = 25;

Servo servo2;
int q2min = 0;
int q2max = 160;

void setup() {
    Serial.begin(9600);
    Serial.println("Hello Arduino!");

    servo2.attach(3);
    servo2.write(q2min);
    delay(delaytime);
}

void loop() {
    for (int i = q2min; i <= q2max; i++) {
        servo2.write(i);
        Serial.println(i);
        delay(delaytime);
    }
    for (int i = q2max; i >= q2min; i--) {
        servo2.write(i);
        Serial.println(i);
        delay(delaytime);
    }
}