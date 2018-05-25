// ----- HELPER FUNCTIONS -----------
int step(float distance){
  int steps = distance * steps_rev / (wheel_dia * 3.1412); //24.61
  return steps;  
}


void moveBackward(float distance){
  int steps = step(distance);
  Serial.println(steps);
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


void done(){ // unlock stepper to save battery
  for(int mask=0; mask<4; mask++){
    for(int pin=0; pin<4; pin++){
      digitalWrite(R_stepper_pins[pin], LOW);
      digitalWrite(L_stepper_pins[pin], LOW);
    }
    delay(delay_time);
  }
  penServo.write(PEN_UP - 20);
  delay(10);
  penServo.detach();
}


void penUp(){
  delay(250);
  Serial.println("PEN_UP()");
  penServo.write(PEN_UP);
  delay(250);
}


void penDown(){
  delay(250);  
  Serial.println("PEN_DOWN()");
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
  while(!(previousAngle <= angle_ && angle_ <= angle)){
    step += 1;
    previousAngle = angle;
    angle = step * step_length * 360 / (wheel_base * 3.1412) + 0.01;
    }
  float dif1 = angle_- angle;
  float dif2 = angle_- previousAngle;
  if(abs(dif1) < abs(dif2)){
    return angle;
  }else{
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


