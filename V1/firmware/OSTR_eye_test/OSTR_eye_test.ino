// Open Source Turtle Robot (OSTR)
// Instructions and licence at https://github.com/aspro648/OSTR

// [Tools] -> [Programmer] -> "USBtinyISP"
// [Tools] -> [Board] -> "Pro Trinket 3V/12 Mhz (USB)"

// Basic test to check IR emitter/detector functionality.
// Front LEDs should light when object present within ~25mm.
// Does not account for IR from sunlight.

// robot setup
byte leftDetector = 19;//A5;
byte leftEmitter = 0;
byte leftLED = A4;
byte rightDetector = 16;//A2;
byte rightEmitter = 9;
byte rightLED = 1;
byte button = A3;

// arrays to help with setup
byte inputs[] = {leftDetector, rightDetector, button};
byte outputs[] = {leftEmitter, leftLED, rightEmitter, rightLED};


void setup() {
  // configure inputs
  for(int input=0; input<(sizeof(inputs)/sizeof(byte)); input++){
    pinMode(inputs[input], INPUT_PULLUP);
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
  pciSetup(rightDetector);
  pciSetup(leftDetector);  
  digitalWrite(rightLED, HIGH);
  digitalWrite(leftLED, HIGH);
}
  

void loop(){ 

  //nothing here, everything handled by interrupt service routine (ISR) below

}


void pciSetup(byte pin){ // set flags for pin to monitor
  *digitalPinToPCMSK(pin) |= bit (digitalPinToPCMSKbit(pin));  // enable pin
  PCIFR  |= bit (digitalPinToPCICRbit(pin)); // clear any outstanding interrupt
  PCICR  |= bit (digitalPinToPCICRbit(pin)); // enable interrupt for the group
}


ISR (PCINT1_vect) { // routine to execute when change detected on pins A0-A5
  //digitalWrite(rightLED, !digitalRead(rightDetector));
  //digitalWrite(leftLED, !digitalRead(leftDetector));
}  
