#include <Servo.h>

int delaytime = 25;

Servo servo3;
int q3min = 0;
int q3max = 180;

void setup() {
    Serial.begin(9600);
    Serial.println("Hello Arduino!");

    servo3.attach(3);
    servo3.write(q3min);
    delay(delaytime);
}

void loop() {
    for (int i = q3min; i <= q3max; i++) {
        servo3.write(i);
        Serial.println(i);
        delay(delaytime);
    }
    for (int i = q3max; i >= q3min; i--) {
        servo3.write(i);
        Serial.println(i);
        delay(delaytime);
    }
}