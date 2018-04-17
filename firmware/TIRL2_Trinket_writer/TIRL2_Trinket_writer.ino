// Download and install Trinket Pro drivers from
// https://learn.adafruit.com/introducing-pro-trinket/starting-the-bootloader

// [Tools] -> [Programmer] -> "USBtinyISP"
// [Tools] -> [Board] -> "Pro Trinket 3V/12 Mhz (USB)"


#include <Servo.h>
typedef int var;        // map javascript datatype to integer
int scale=10; //   # Scale for letters, 2.5x = 5cm x 10cm 

// setup servo
int servoPin = 8;
int PEN_DOWN = 130;     // angle of servo when pen is down
int PEN_UP = 70;        // angle of servo when pen is up
Servo penServo;

float wheel_dia=59;     //   mm (increase = decrease distance
float wheel_base=79.75;  //   mm (increase = spiral in) 
int steps_rev=512;      //   512 for 64x gearbox, 128 for 16x gearbox
int delay_time=2;       //   time between steps in ms

// Stepper sequence org->pink->blue->yel
int L_stepper_pins[] = {10, 12, 13, 11};
int R_stepper_pins[] = {4, 6, 5, 3};      //PD4, PD6, PD5, PD3

//                0b76543210
byte L_seq[4] = { B00100100,  //port PB
                  B00110000,
                  B00011000,
                  B00001100};

byte R_seq[4] = { B00011000,  // port PD
                  B01001000,
                  B01100000,
                  B00110000};


void setup() {
  randomSeed(analogRead(A2)); 
  for(int pin=0; pin<4; pin++){
    pinMode(L_stepper_pins[pin], OUTPUT);
    digitalWrite(L_stepper_pins[pin], LOW);
    pinMode(R_stepper_pins[pin], OUTPUT);
    digitalWrite(R_stepper_pins[pin], LOW);
  }
  penServo.attach(servoPin);
}


void spiral(int size, int angle){ // inward spiral
  while(size > 0){
    forward(size);
    right(angle);
    size = size -2;
  }
}


void loopTest(){ // draw a calibration box 4 times
  for(int x=0; x<12; x++){
    forward(100);
    left(90);
  }
  while(1){}
}


void loop() {
  pendown();
  A();
  D();
  A();
  f();
  R();
  U();
  I();
  T();

  left(90);
  backward(5 * scale);
  right(90);
  backward(4 * scale * 4);
  R();
  O();
  C();
  K();
  S();
  forward(5.5 * scale);
  left(180);
  while(1);
}

