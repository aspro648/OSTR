// Open Source Turtle Robot (OSTR)
// Instructions and licence at https://github.com/aspro648/OSTR

// [Tools] -> [Programmer] -> "USBtinyISP"
// [Tools] -> [Board] -> "Pro Trinket 3V/12 Mhz (USB)"

// Draws four 100mm squares for calibration


#include <Servo.h>
typedef int var;        // map javascript datatype to integer

// setup servo
int servoPin = 8;
int PEN_DOWN = 150;     // angle of servo when pen is down
int PEN_UP = 90;        // angle of servo when pen is up
Servo penServo;

// robot specific parameters
float wheel_dia=52;     //   mm (increase = decrease distance
float wheel_base=73.75; //   mm (increase = spiral in) 
float angle_error = 0;
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

//               0b76543210
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
  Serial.begin(9600);
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


void loop(){ // draw a calibration box 4 times
  penDown();
  //circle(100);
  //penUp();
  //while(1){};
  for(int x=0; x<16; x++){
    moveForward(100);
    turnRight(90);
  }
  penUp();
  done();      // releases stepper motor
  while(1);    // wait for reset
}


// ----- HELPER FUNCTIONS -----------
int step(float distance){
  float steps = distance * steps_rev / (wheel_dia * 3.1412); //24.61
  return int(steps);  
}


void moveBackward(float distance){
  int steps = step(distance);
  for(int step=0; step<steps; step++){
    for(int mask=0; mask<4; mask++){
      PORTB = PORTB | L_seq[mask];
      PORTD = PORTD | R_seq[mask];
      delay(delay_time);
      PORTB = PORTB & ~L_seq[mask];
      PORTD = PORTD & ~R_seq[mask];
    } 
  }
}


void moveForward(float distance){
  int steps = step(distance);
  for(int step=0; step<steps; step++){
    for(int mask=0; mask<4; mask++){
      PORTB = PORTB | L_seq[3-mask];
      PORTD = PORTD | R_seq[3-mask];
      delay(delay_time);
      PORTB = PORTB & ~L_seq[mask];
      PORTD = PORTD & ~R_seq[mask];
    } 
  }
}


void turnLeft(float degrees){
  //float rotation = degrees / 360.0;
  float rotation = getNearestAngle(degrees) / 360.0;
  float distance = wheel_base * 3.1412 * rotation;
  int steps = step(distance);
  for(int step=0; step<steps; step++){
    for(int mask=0; mask<4; mask++){
      PORTB = PORTB | L_seq[3 - mask];
      PORTD = PORTD | R_seq[mask];
      delay(delay_time);
      PORTB = PORTB & ~L_seq[3 - mask];
      PORTD = PORTD & ~R_seq[mask];
    } 
  }   
}


void turnRight(float degrees){
  //float rotation = degrees / 360.0;
  float rotation = getNearestAngle(degrees) / 360.0;
  float distance = wheel_base * 3.1412 * rotation;
  int steps = step(distance);
  for(int step=0; step<steps; step++){
    for(int mask=0; mask<4; mask++){
      PORTB = PORTB | L_seq[mask];
      PORTD = PORTD | R_seq[3-mask];
      delay(delay_time);
      PORTB = PORTB & ~L_seq[mask];
      PORTD = PORTD & ~R_seq[3-mask];
    } 
  }   
}


void circle(int diameter){
  int circumference = diameter * 3.1412;
  int sides = 10+diameter/3.0;
  Serial.println(sides);
  if(sides>20){
    sides=20;
  }
  float length = circumference / sides;
  for(int x=0; x<sides; x++){
    moveForward(length);
    turnRight(360/sides);
  }
}


void done(){ // unlock stepper to save battery
  for(int mask=0; mask<4; mask++){
    for(int pin=0; pin<4; pin++){
      digitalWrite(R_stepper_pins[pin], LOW);
      digitalWrite(L_stepper_pins[pin], LOW);
    }
  }
  penServo.write(PEN_UP - 20);
  delay(10);
  penServo.detach();
}


void penUp(){
  delay(250);
  penServo.write(PEN_UP);
  delay(250);
}


void penDown(){
  delay(250);  
  penServo.write(PEN_DOWN);
  delay(250);
}


float getNearestAngle(float angle_){ 
  // code contributed by Instructable user PMPU_student
  /*
  Lets rotate by 58 degrees.
  turnRight(58); // rotate only by 57.631138392857146 degrees(that is the 
  value that is the closest to the desired one _and_ is lesser than it). 
  That means you are doing a certain amount of motor steps. But if you do 
  one more step during rotation you will rotate by 58.0078125 degrees, 
  which is much more precise(but it is greater than desired value, thats 
  why in original code it is not picked). The thing is that original code 
  always decides to rotate by value that is lesser than desired value while 
  it is sometimes worse than choosing the value that is bigger. 
  My code chooses from both variants, minimizing the error.
  */
  float angle = 0;
  int step = 0;
  float previousAngle = 0;
  float step_length = 3.1412 * wheel_dia / steps_rev;
  //angle_ += angle_error;
  while(!(previousAngle <= angle_ && angle_ <= angle)){
    step += 1;
    previousAngle = angle;
    angle = step * step_length * 360 / (wheel_base * 3.1412) + 0.01;
    }
  float dif1 = angle_- angle;
  float dif2 = angle_- previousAngle;
  if(abs(dif1) < abs(dif2)){
    angle_error = dif1;
    Serial.println(angle_error);
    return angle;
  }else{
    angle_error = dif2;
    Serial.println(angle_error);
    return previousAngle;
  }
}


//Aliases for compatiblity with other Turtle program's commands

void forward(float distance){
  moveForward(distance);
}

void backward(float distance){
  moveBackward(distance);
}

void left(float angle){
  turnLeft(angle);
}

void right(float angle){
  turnRight(angle);
}

void penup(){
  penUp();
}

void pendown(){
  penDown();
}

void fd(float distance){
  moveForward(distance);
}

void bk(float distance){
  moveBackward(distance);
}

void lt(float angle){
  turnLeft(angle);
}

void rt(float angle){
  turnRight(angle);
}

void pu(){
  penUp();
}

void pd(){
  penDown();
}





