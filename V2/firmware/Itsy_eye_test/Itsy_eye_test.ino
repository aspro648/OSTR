// Open Source Turtle Robot (OSTR)
// Instructions and licence at https://github.com/aspro648/OSTR

// [Tools] -> [Programmer] -> "USBtinyISP"
// [Tools] -> [Board] -> "Adafruit ItsyBitsy 32U4 3V 8 MHz"

// Basic test to check IR emitter/detector functionality.
// Front LEDs should light when object present within ~25mm.
// Does not account for IR from sunlight.

// robot setup
byte leftDetector = A1; // SCL INT0
byte leftEmitter = 10;
byte leftLED = 7;
byte rightDetector = A0;  // SDA INT1
byte rightEmitter = 13;
byte rightLED = 11;
byte button = 12;

// arrays to help with setup
byte inputs[] = {leftDetector, rightDetector, button};
byte outputs[] = {leftEmitter, leftLED, rightEmitter, rightLED};


void setup() {
  // configure inputs
  for(int input=0; input<(sizeof(inputs)/sizeof(byte)); input++){
    pinMode(inputs[input], INPUT);
  }  
  // configure outputs
  for(int output=0; output<(sizeof(outputs)/sizeof(byte)); output++){
    pinMode(outputs[output], OUTPUT);
    digitalWrite(output, LOW);
  }
  // turn on IR emitters
  digitalWrite(rightEmitter, HIGH);
  digitalWrite(leftEmitter, HIGH);
  
  // setup pins for pin change interrupt
  //pciSetup(rightDetector);
  //pciSetup(leftDetector);  
  //attachInterrupt(digitalPinToInterrupt(leftDetector), blink, CHANGE);
  //attachInterrupt(digitalPinToInterrupt(rightDetector), blink, CHANGE);

  Serial.begin(9600);
  Serial.println("eye_test");
}
  

void loop(){ 

  //nothing here, everything handled by interrupt service routine (ISR) below
  int leftVal = analogRead(leftDetector);
  int rightVal = analogRead(rightDetector);

  Serial.print(leftVal);
  Serial.print(" ");
  Serial.println(rightVal);

  delay(100);
 

}


void pciSetup(byte pin){ // set flags for pin to monitor
  *digitalPinToPCMSK(pin) |= bit (digitalPinToPCMSKbit(pin));  // enable pin
  PCIFR  |= bit (digitalPinToPCICRbit(pin)); // clear any outstanding interrupt
  PCICR  |= bit (digitalPinToPCICRbit(pin)); // enable interrupt for the group
}


ISR (PCINT1_vect) { // routine to execute when change detected on pins A0-A5
  digitalWrite(rightLED, !digitalRead(rightDetector));
  digitalWrite(leftLED, !digitalRead(leftDetector));
}  


void blink(){
  digitalWrite(rightLED, !digitalRead(rightDetector));
  digitalWrite(leftLED, !digitalRead(leftDetector));
}

