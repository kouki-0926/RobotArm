const int SW_pin = 2;
const int X_pin = 0;
const int Y_pin = 1;

void init_Joystick() { pinMode(SW_pin, INPUT_PULLUP); }

void send() {
    Serial.print(digitalRead(SW_pin));
    Serial.print(",");
    Serial.print(analogRead(X_pin));
    Serial.print(",");
    Serial.println(analogRead(Y_pin));
}

#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

int q1pin = 3;
int q2pin = 5;
int q3pin = 6;
int q4pin = 9;
int q5pin = 10;
int q6pin = 11;

int add = 0;
int input = -1;
int sign = 1;

void init_servo() {
    servo1.attach(q1pin);
    servo2.attach(q2pin);
    servo3.attach(q3pin);
    servo4.attach(q4pin);
    servo5.attach(q5pin);
    servo6.attach(q6pin);

    servo1.write(146);
    servo2.write(90);
    servo3.write(90);
    servo4.write(75);
    servo5.write(0);
    servo6.write(0);
}

void receive() {
    input = Serial.read();
    if (input != -1) {
        switch (input) {
            case '-':
                sign = -1;
                break;
            case '0':
                add = 0 + add * 10;
                break;
            case '1':
                add = 1 + add * 10;
                break;
            case '2':
                add = 2 + add * 10;
                break;
            case '3':
                add = 3 + add * 10;
                break;
            case '4':
                add = 4 + add * 10;
                break;
            case '5':
                add = 5 + add * 10;
                break;
            case '6':
                add = 6 + add * 10;
                break;
            case '7':
                add = 7 + add * 10;
                break;
            case '8':
                add = 8 + add * 10;
                break;
            case '9':
                add = 9 + add * 10;
                break;
            case 'a':
                servo1.write(146 + sign * add);
                add = 0;
                sign = 1;
                break;
            case 'b':
                servo2.write(-sign * add);
                add = 0;
                sign = 1;
                break;
            case 'c':
                servo3.write(-sign * add + 90);
                add = 0;
                sign = 1;
                break;
            case 'd':
                servo4.write(sign * add);
                add = 0;
                sign = 1;
                break;
            case 'e':
                servo5.write(sign * add);
                add = 0;
                sign = 1;
                break;
            case 'f':
                servo6.write(sign * add);
                add = 0;
                sign = 1;
                break;
            default:
                break;
        }
    }
}

// #define MANUAL

void setup() {
#ifdef MANUAL
    init_Joystick();
#endif
    init_servo();
    Serial.begin(115200);
}

void loop() {
#ifdef MANUAL
    send();
    delay(75);
#endif
    receive();
}