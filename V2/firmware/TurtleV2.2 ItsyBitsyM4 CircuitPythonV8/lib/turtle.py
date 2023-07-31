'''
Ver 20200304
Ver 20210515 Allow for reversing turtle orientation
Ver 20230719 Pins designations to settings.py, stepper pin nomiclature changed,
             added _rotate() and speed() functions.
'''

import math
import time
import digitalio
from analogio import AnalogIn
from adafruit_motor import servo
from time import sleep
import pwmio
import settings

print('The following parameters are saved in "lib/settings.py":')
print('    wheel_dia = %s mm (increase = decrease distance)' % settings.wheel_dia)
print('    wheel_base = %s mm (increase = spiral in) ' % settings.wheel_base)
print('    PEN_UP angle = %s' % settings.PEN_UP)
print('    PEN_DOWN angle = %s' % settings.PEN_DOWN)

# create a PWMOut and servo object
pwm = pwmio.PWMOut(settings.servoPin, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(pwm, min_pulse=settings.min_pulse, max_pulse=settings.max_pulse)

DEBUG = settings.DEBUG

delay_time = settings.delay_time

# Pin assignments
emitter = digitalio.DigitalInOut(settings.emitterPin)
leftLED = digitalio.DigitalInOut(settings.leftLEDPin)
rightLED = digitalio.DigitalInOut(settings.rightLEDPin)
button = digitalio.DigitalInOut(settings.buttonPin)
rightDetector = AnalogIn(settings.rightDetectorPin)
leftDetector = AnalogIn(settings.leftDetectorPin)

# Port setup
emitter.direction = digitalio.Direction.OUTPUT
leftLED.direction = digitalio.Direction.OUTPUT
rightLED.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# [wires blue->pink->yel->org]
L_In1 = digitalio.DigitalInOut(settings.L_In1_Pin)
L_In2 = digitalio.DigitalInOut(settings.L_In2_Pin)
L_In3 = digitalio.DigitalInOut(settings.L_In3_Pin)
L_In4 = digitalio.DigitalInOut(settings.L_In4_Pin)

R_In1 = digitalio.DigitalInOut(settings.R_In1_Pin)
R_In2 = digitalio.DigitalInOut(settings.R_In2_Pin)
R_In3 = digitalio.DigitalInOut(settings.R_In3_Pin)
R_In4 = digitalio.DigitalInOut(settings.R_In4_Pin)

# put connections in List to make life easier
R_stepper = [R_In1, R_In2, R_In3, R_In4]
L_stepper = [L_In1, L_In2, L_In3, L_In4]

for wire in L_stepper:
    wire.direction = digitalio.Direction.OUTPUT

for wire in R_stepper:
    wire.direction = digitalio.Direction.OUTPUT

# stepper patterns
patterns = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]

_x = 0
_y = 0
_heading = 0
_angular_error = 0


def setDebug(val):
    global DEBUG
    DEBUG = val


def dist(steps):
    return steps * (settings.wheel_dia * math.pi) / settings.steps_rev


def step(distance):
    steps = distance * settings.steps_rev/(settings.wheel_dia * math.pi)
    return round(steps), 0


def forward(distance):
    global _x, _y, _heading
    steps, frac = step(distance)
    if DEBUG:
        print("forward(%s)" % distance)

    for x in range(steps):
        for pattern in range(len(patterns)):
            for bit in range(len(patterns[pattern])):  # fwd_mask[num]:
                if settings.invert_direction:
                    L_stepper[bit].value = patterns[pattern][bit]
                    R_stepper[bit].value = patterns[::-1][pattern][bit]
                else:
                    R_stepper[bit].value = patterns[pattern][bit]
                    L_stepper[bit].value = patterns[::-1][pattern][bit]
            time.sleep(delay_time/1000)

    # new point
    deltax = distance * math.cos(math.radians(_heading))
    deltay = distance * math.sin(math.radians(_heading))
    _x = _x + deltax
    _y = _y + deltay


def backward(distance):
    global _x, _y, _heading
    steps, frac = step(distance)
    if DEBUG:
        print("backward(%s)" % distance)

    for x in range(steps):
        for pattern in range(len(patterns)):
            for bit in range(len(patterns[pattern])):  # fwd_mask[num]:
                if settings.invert_direction:
                    R_stepper[bit].value = patterns[pattern][bit]
                    L_stepper[bit].value = patterns[::-1][pattern][bit]
                else:
                    L_stepper[bit].value = patterns[pattern][bit]
                    R_stepper[bit].value = patterns[::-1][pattern][bit]
            time.sleep(delay_time/1000)

    # new point
    deltax = distance * math.cos(math.radians(_heading - 180))
    deltay = distance * math.sin(math.radians(_heading - 180))
    _x = _x + deltax
    _y = _y + deltay


def left(degrees):
    """Turn turlte left by number of degrees."""
    if DEBUG:
        print("left(%s)" % degrees)
    _rotate(-degrees)


def right(degrees):
    """Turn turlte right by number of degrees."""
    if DEBUG:
        print("right(%s)" % degrees)
    _rotate(degrees)


def _rotate(degrees):
    global _x, _y, _heading, _angular_error
    #if settings.invert_direction:
    #    degrees = - degrees
    print("rotate(%s)" % degrees)
    rotation = (degrees) / 360.0
    distance = settings.wheel_base * math.pi * rotation
    steps, frac = step(distance)
    if False:
        print("    degrees = %s" % degrees)
        print("    rotation = %s" % rotation)
        print("    distance = %s" % distance)
        print("    steps = %s" % steps)
        print("    distance = %s" % dist(steps))
        distance_error = dist(steps) - distance
        print("    distance_error = %s" % distance_error)
        rotation_error = distance_error / settings.wheel_base / math.pi
        print("    rotation_error = %s" %  rotation_error)
        angular_error = rotation_error * 360
        _angular_error += angular_error
        print("    angular_error = %s" % _angular_error)
    for x in range(abs(steps)):
        for pattern in range(len(patterns)):
            for bit in range(len(patterns[pattern])):  # fwd_mask[num]:
                if degrees < 0:
                    if settings.invert_direction:
                        R_stepper[bit].value = patterns[pattern][bit]
                        L_stepper[bit].value = patterns[pattern][bit]
                    else:
                        R_stepper[bit].value = patterns[::-1][pattern][bit]
                        L_stepper[bit].value = patterns[::-1][pattern][bit]
                else:
                    if settings.invert_direction:
                        R_stepper[bit].value = patterns[::-1][pattern][bit]
                        L_stepper[bit].value = patterns[::-1][pattern][bit]
                    else:
                        R_stepper[bit].value = patterns[pattern][bit]
                        L_stepper[bit].value = patterns[pattern][bit]
            time.sleep(delay_time/1000)
    _heading = _heading - degrees
    while _heading > 360:
        _heading = _heading - 360
    while _heading < 0:
        _heading = _heading + 360


def penup():
    servo.angle = settings.PEN_UP
    if DEBUG:
        print("penup()")
    sleep(0.25)


def pendown():
    servo.angle = settings.PEN_DOWN
    if DEBUG:
        print("pendown()")
    sleep(0.5)


def done():
    for value in range(4):
        L_stepper[value].value = False
        R_stepper[value].value = False
    penup()
    time.sleep(1)
    if DEBUG:
        print("done()")


def goto(x, y):
    center_x, center_y = position()

    bearing = getBearing(x, y, center_x, center_y)
    trnRight = heading() - bearing
    if DEBUG:
        print("goto(%s, %s)" % (x, y))
        print('    start position =', position())
    if abs(trnRight) > 180:
        if trnRight >= 0:
            left(360 - trnRight)
            #if DEBUG: print('left(%s)' % (360 - trnRight))
        else:
            right(360 + trnRight)
            #if DEBUG: print('right(%s)' % (360 + trnRight))
    else:
        if trnRight >= 0:
            right(trnRight)
            #if DEBUG: print('right(%s)' % trnRight)
        else:
            left(-trnRight)
            #if DEBUG: print('left(%s)' % -trnRight)
    dist = distance(tuple(position()), (x, y))
    forward(dist)
    #if DEBUG: print('forward(%s)' % distance)
    print('    heading = %s' % heading())
    print('    end position =', position())


def setheading(to_angle):
    '''
    Set the orientation of the turtle to to_angle.

    Aliases:  setheading | seth

    Argument:
    to_angle -- a number (integer or float)

    Set the orientation of the turtle to to_angle.
    Here are some common directions in degrees:

     standard - mode:          logo-mode:
    -------------------|--------------------
       0 - east                0 - north
      90 - north              90 - east
     180 - west              180 - south
     270 - south             270 - west

    Example:
    >>> setheading(90)
    >>> heading()
    90
    '''

    cur_heading = heading()
    if (to_angle - cur_heading) < 0:
        if (to_angle - cur_heading) > -180:
            left(to_angle - cur_heading)
            if DEBUG: print("Case 1 left(%s)" % (to_angle - cur_heading))
        else:
            left(to_angle - cur_heading + 360)
            if DEBUG: print("Case 2 left(%s)" % (to_angle - cur_heading + 360))
    else:
        if (to_angle - cur_heading) > 180:
            left(360 - to_angle - cur_heading - 180)
            if DEBUG: print("Case 3 left(%s)" % (360 - to_angle - cur_heading))
        else:
            left(to_angle - cur_heading)
            if DEBUG: print("Case 4 left(%s)" % (to_angle - cur_heading))


def pensize(size):
    if DEBUG: print('pensize() is not implemented in Turtle Robot')


def pencolor(color):
    if DEBUG: print('pencolor() is not implemented in Turtle Robot')


def speed(x):
    if DEBUG: print('speed() is not implemented in Turtle Robot')


def shape(x):
    if DEBUG: print('shape() is not implemented in Turtle Robot')


def color(x):
    if DEBUG: print('color() is not implemented in Turtle Robot')


def position():
    return _x, _y


def heading():
    return _heading


def distance(pointA, pointB):
    return abs((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2)**0.5


def getBearing(x, y, center_x, center_y):
    # https://stackoverflow.com/questions/5058617/bearing-between-two-points
    angle = math.degrees(math.atan2(y - center_y, x - center_x))
    bearing = (angle + 360) % 360
    return bearing


def circle(radius, extent=None, steps=None):
    """ Draw a circle with given radius.

    Arguments:
    radius -- a number
    extent (optional) -- a number
    steps (optional) -- an integer

    Draw a circle with given radius. The center is radius units left
    of the turtle; extent - an angle - determines which part of the
    circle is drawn. If extent is not given, draw the entire circle.
    If extent is not a full circle, one endpoint of the arc is the
    current pen position. Draw the arc in counterclockwise direction
    if radius is positive, otherwise in clockwise direction. Finally
    the direction of the turtle is changed by the amount of extent.

    As the circle is approximated by an inscribed regular polygon,
    steps determines the number of steps to use. If not given,
    it will be calculated automatically. Maybe used to draw regular
    polygons.

    call: circle(radius)                  # full circle
    --or: circle(radius, extent)          # arc
    --or: circle(radius, extent, steps)
    --or: circle(radius, steps=6)         # 6-sided polygon

    Example (for a Turtle instance named turtle):
    >>> turtle.circle(50)
    >>> turtle.circle(120, 180)  # semicircle
    """

    if extent is None:
        extent = 360
    if steps is None:
        frac = abs(extent)/360
        # print("frac = %s" % frac)
        steps = 1+int(min(11+abs(radius)/6.0, 59.0)*frac)
    w = 1.0 * extent / steps
    w2 = 0.5 * w
    length = 2.0 * radius * math.sin(w2*math.pi/180.0)
    if radius < 0:
        length, w, w2 = -length, -w, -w2
    if DEBUG:
        print("circle(%s, extent=%s, steps=%s)" % (radius, extent, steps))
    if False:
        print("length (step length) = %s" % length)
        print("w (turn angle)= %s" % w)		
        print("w2 (inital rotation) = %s" % w2)

        print("steps = %s" % steps)	
        print("extent = %s" % extent)
        # print("self._degreesPerAU = %s" % self._degreesPerAU)
    left(w2)
    for i in range(steps):
        forward(length)
        left(w)
    left(-w2)


def speed(speed=None):
    '''
    speed(speed=None)

        Return or set the turtle's speed.

        Optional argument:
        speed -- an integer in the range 0..10 or a speedstring (see below)

        Set the turtle's speed to an integer value in the range 0 .. 10.
        If no argument is given: return current speed.

        If input is a number greater than 10 or smaller than 0.5,
        speed is set to 0.
        Speedstrings  are mapped to speedvalues in the following way:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6
            'slow'    :  3
            'slowest' :  1
        speeds from 1 to 10 enforce increasingly faster animation of
        line drawing and turtle turning.

        Note:
        Robot's speed controlled by delay_time.  Delay_time less than 2ms
        will stall motor.

        Example:
    speed(3)
    '''
    global delay_time
    speeds = {'fastest':0, 'fast':10, 'normal':6, 'slow':3, 'slowest':1 }
    if speed is None:
        if delay_time == 2:
            return 0
        else:
            return 13 - delay_time
    if speed in speeds:
        speed = speeds[speed]
    elif 0.5 < speed < 10.5:
        speed = int(round(speed))
    else:
        speed = 0
    if speed == 0:
        delay_time = 2
    else:
        delay_time = 13 - speed
    if DEBUG: print("delay_time = %s" % delay_time)


def isButtonPushed():
    return not button.value #pulled up (True) when not pushed


def drawPage():
    #boarder of 8.5 x 11 in paper
    pageX = 280
    pageY = 216
    penup()
    goto(-pageX/2, -pageY/2)
    pendown()
    goto(-pageX/2, pageY/2)
    goto(pageX/2, pageY/2)
    goto(pageX/2, -pageY/2)
    goto(-pageX/2, -pageY/2)
    penup()
    goto(0,0)


