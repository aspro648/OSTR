# robot specific parameters
wheel_dia = 51     # mm (increase = decrease distance)
wheel_base = 71.9 # mm (increase = spiral clockwise)

# stepper parameters
steps_rev = 512    # 512 for 64x gearbox, 128 for 16x gearbox
delay_time = 3     # time between steps in ms (too quick will freeze motors)

# servo parameters
PEN_DOWN = 170     # angle of servo when pen is down
PEN_UP = 85        # angle of servo when pen is up
min_pulse = 750
max_pulse = 2500
