// Open Source Turtle Robot (OSTR)
// Instructions and licence at https://github.com/aspro648/OSTR

// [Tools] -> [Programmer] -> "USBtinyISP"
// [Tools] -> [Board] -> "Pro Trinket 3V/12 Mhz (USB)"

// Writes letters using a simple vector font.
// Place Turtle in center of 8.5 x 11" landscape paper
// with turtle facing right.


#include <Servo.h>
typedef int var;        // map javascript datatype to integer
int scale=15; //   # Scale for letters, 2.5x = 5cm x 10cm 

// setup servo
int servoPin = 8;
int PEN_DOWN = 160;     // angle of servo when pen is down
int PEN_UP = 90;        // angle of servo when pen is up
Servo penServo;

// robot specific parameters
float wheel_dia=51.75;     //   mm (increase = decrease distance
float wheel_base=72.75; //   mm (increase = spiral in) 
byte leftDetector = A5;
byte leftEmitter = 0;
byte leftLED = A4;
byte rightDetector = A2;
byte rightEmitter = 9;
byte rightLED = 1;
byte button = A3;

// Stepper parameters 
int steps_rev=512;      //   512 for 64x gearbox, 128 for 16x gearbox
int delay_time=2;       //   time between steps in ms
int L_stepper_pins[] = {10, 12, 13, 11};  //PB2, PB4, PB5, PB3 [wires org->pink->blue->yel]
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

// arrays to help with setup
byte inputs[] = {leftDetector, rightDetector, button};
byte outputs[] = {leftEmitter, leftLED, rightEmitter, rightLED, servoPin};


void setup() {
  randomSeed(analogRead(A3));  // randomize on floating input
  for(int pin=0; pin<4; pin++){
    pinMode(L_stepper_pins[pin], OUTPUT);
    digitalWrite(L_stepper_pins[pin], LOW);
    pinMode(R_stepper_pins[pin], OUTPUT);
    digitalWrite(R_stepper_pins[pin], LOW);
  }

  // configure inputs
  for(int input=0; input<(sizeof(inputs)/sizeof(byte)); input++){
    pinMode(inputs[input], INPUT_PULLUP);
  }  

  // configure outputs
  for(int output=0; output<(sizeof(outputs)/sizeof(byte)); output++){
    pinMode(outputs[output], OUTPUT);
    digitalWrite(output, LOW);
  }

  penServo.attach(servoPin);
  penUp();
}


void spiral(int size, int angle){ // inward spiral
  while(size > 0){
    moveForward(size);
    turnRight(angle);
    size = size -2;
  }
}


void loopTest(){ // draw a calibration box 4 times
  for(int x=0; x<12; x++){
    moveForward(100);
    turnLeft(90);
  }
  while(1){}
}


void loop() {
  // assume starting in center of 8.5 x 11" page
  scale = 12;
  
  // move into position
  turnLeft(45);
  moveBackward(1.41 * scale * 2);
  turnRight(45);
  moveBackward(6 * scale);

  T();
  U();
  R();
  T();
  L();
  E();
  ex();

  penUp();
  moveForward(100);
  while(1);
}

