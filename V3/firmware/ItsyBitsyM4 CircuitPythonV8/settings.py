# robot specific parameters
wheel_dia = 57     # mm (increase = decrease distance)
wheel_base = 106.8  # mm (increase = spiral clockwise)

# stepper parameters
steps_rev = 512    # 512 for 64x gearbox, 128 for 16x gearbox
delay_time = 2     # time between steps in ms (too quick will freeze motors)
invert_direction = False  # change if turtle running backward

# servo parameters
PEN_DOWN = 75     # angle of servo when pen is down
PEN_UP = 160      # angle of servo when pen is up
min_pulse = 750
max_pulse = 2500

DEBUG = True      # Print statements to console

import board

if False: # pins for IstyBitsy M4 Breadboard Robot
    servoPin = board.D7
    speakerPin = board.D5
    buttonPin = board.MISO

    leftLEDPin = board.A2
    rightLEDPin = board.A3
    emitterPin = board.A1

    rightDetectorPin = board.A4
    leftDetectorPin = board.A5

    L_In1_Pin = board.D13  # has onboard LED on it
    L_In2_Pin = board.D12
    L_In3_Pin = board.D11
    L_In4_Pin = board.D10

    R_In1_Pin = board.SCL
    R_In2_Pin = board.SDA
    R_In3_Pin = board.D1
    R_In4_Pin = board.D0

else: # pins for Turtle Robot Base Kit
    servoPin = board.A1
    speakerPin = board.A0
    buttonPin = board.D12

    leftLEDPin = board.D7
    rightLEDPin = board.D11
    emitterPin = board.D5

    rightDetectorPin = board.A2
    leftDetectorPin = board.A3

    L_In1_Pin = board.D13  # has onboard LED on it
    L_In2_Pin = board.D10
    L_In3_Pin = board.A4
    L_In4_Pin = board.A5

    R_In1_Pin = board.SCK
    R_In2_Pin = board.MOSI
    R_In3_Pin = board.MISO
    R_In4_Pin = board.D9
