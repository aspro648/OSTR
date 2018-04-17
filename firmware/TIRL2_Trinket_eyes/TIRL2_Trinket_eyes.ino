// Download and install Trinket Pro drivers from
// https://learn.adafruit.com/introducing-pro-trinket/starting-the-bootloader

// [Tools] -> [Programmer] -> "USBtinyISP"
// [Tools] -> [Board] -> "Pro Trinket 3V/12 Mhz (USB)"


#include <Servo.h>
typedef int var;         // map javascript datatype to integer

// setup servo
int servoPin = 8;
int PEN_DOWN = 140;      // angle of servo when pen is down
int PEN_UP = 90;         // angle of servo when pen is up
Servo penServo;

float wheel_dia=58.4;    // mm (increase = spiral out)
float wheel_base=80;     // mm (increase = spiral in) 
int steps_rev=512;       // 512 for 64x gearbox, 128 for 16x gearbox
int delay_time=2;        // time between steps in ms

// Stepper sequence org->pink->blue->yel
int L_stepper_pins[] = {10, 12, 13, 11};  //PB2, PB4, PB5, PB3
int R_stepper_pins[] = {4, 6, 5, 3};      //PD4, PD6, PD5, PD3

int leftSensor = A4;
int leftLight = A0;
int rightSensor = A1;
int rightLight = A5;
int threashold = 200;

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
  
  pinMode(leftSensor, INPUT_PULLUP);
  pinMode(leftLight, OUTPUT);
  pinMode(rightSensor, INPUT_PULLUP);
  pinMode(rightLight, OUTPUT);
  
  //penServo.attach(servoPin);
}


void loop(){ // draw a calibration box 4 times
  //pendown();

  bool wallLeft = wallDetect(leftSensor, leftLight);
  bool wallRight = wallDetect(rightSensor, rightLight);
  
  if(!wallLeft && !wallRight){
    forward(1);
  }
  else{
    backward(1);
    if(wallLeft && !wallRight){
      right(10);
    }
    else if(wallRight && !wallLeft){
      left(10);
    }
    else{
      if(random(1)){
        right(random(180));
      }
      else{
        left(random(180));
      }
    }
  }
  
}


// ----- HELPER FUNCTIONS -----------

bool wallDetect(int sensorPin, int lightPin){
  int val1 = analogRead(sensorPin);
  digitalWrite(lightPin, HIGH);
  int val2 = analogRead(sensorPin);
  digitalWrite(lightPin, LOW);
  if ((val1 - val2) > threashold){
    return(true);
  }
  else {
    return(false);
  }
}
  



int step(float distance){
  int steps = distance * steps_rev / (wheel_dia * 3.1412); //24.61
  return steps;  
}


void forward(float distance){
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


void backward(float distance){
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


void left(float degrees){
  float rotation = degrees / 360.0;
  float distance = wheel_base * 3.1412 * rotation;
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


void right(float degrees){
  float rotation = degrees / 360.0;
  float distance = wheel_base * 3.1412 * rotation;
  int steps = step(distance);
  for(int step=0; step<steps; step++){
    for(int mask=0; mask<4; mask++){
      PORTB = PORTB | L_seq[3-mask];
      PORTD = PORTD | R_seq[3-mask];
      delay(delay_time);
      PORTB = PORTB & ~L_seq[3-mask];
      PORTD = PORTD & ~R_seq[3-mask];
    } 
  }   
}


void done(){ // unlock stepper to save battery
  for(int mask=0; mask<4; mask++){
    for(int pin=0; pin<4; pin++){
      digitalWrite(R_stepper_pins[pin], LOW);
      digitalWrite(L_stepper_pins[pin], LOW);
    }
    delay(delay_time);
  }
}


void penup(){
  delay(250);
  penServo.write(PEN_UP);
  delay(250);
}


void pendown(){
  delay(250);  
  penServo.write(PEN_DOWN);
  delay(250);
}

