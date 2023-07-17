# Mash-up of code from:
# https://docs.circuitpython.org/projects/httpserver/en/latest/examples.html
# (2022 Dan Halbert for Adafruit Industries)

# https://learn.adafruit.com/pico-w-http-server-with-circuitpython/code-the-pico-w-http-server
# (2023 Liz Clark for Adafruit Industries)

import socketpool
import wifi
import board

from adafruit_httpserver import Server, Request, Response, POST
from digitalio import DigitalInOut, Direction


# Attach an LED and resistor to GPIO16
# (The Pico W onboard LED is not connected to a GPIO on the RP2040,
# it’s connected to a GPIO on the WiFi/BLE so the normal
# "led = digitalio.DigitalInOut(board.LED)" method will not work.)
led = DigitalInOut(board.GP16)
led.direction = Direction.OUTPUT
led.value = True

# Network interface (wifi details are in setting.toml file)
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)


#  route default static IP
@server.route("/")
def base(request: Request):
    #  serve the HTML f string with content type text/html
    return Response(request, f"{webpage()}", content_type='text/html')


#  if a button is pressed on the site
@server.route("/", POST)
def buttonpress(request: Request):
    #  get the raw text
    raw_text = request.raw_request.decode("utf8")
    print(raw_text)
    #  if the led on button was pressed
    if "ON" in raw_text:
        #  turn on the onboard LED
        led.value = True
    #  if the led off button was pressed
    if "OFF" in raw_text:
        #  turn the onboard LED off
        led.value = False
    #  reload site
    return Response(request, f"{webpage()}", content_type='text/html')


#  the HTML script setup as an f string
#  this way, can insert string variables from code.py directly
#  of note, use {{ and }} if something from html *actually* needs to be in brackets
#  i.e. CSS style formatting
def webpage():
    font_family = "monospace"

    # form button based on state of LED
    if led.value:
        button = '''<button class="button" name="LED" value="OFF" type="submit">TURN OFF</button>'''
    else:
        button = '''<button class="button" name="LED" value="ON" type="submit">TURN  ON</button>'''

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-type" content="text/html;charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    html{{font-family: {font_family}; background-color: lightgrey;
    display:inline-block; margin: 0px auto; text-align: center;}}
      h1{{color: deeppink; width: 200; word-wrap: break-word; padding: 2vh; font-size: 35px;}}
      p{{font-size: 1.5rem; width: 200; word-wrap: break-word;}}
      .button{{font-family: {font_family};display: inline-block;
      background-color: black; border: none;
      border-radius: 4px; color: white; padding: 10px 20px;
      text-decoration: none; font-size: 20px; margin: 2px; cursor: pointer;}}
      .resizedTextbox {{width: 100px; height: 40px; padding: 1px}}
      p.dotted {{margin: auto;
      width: 75%; font-size: 25px; text-align: center;}}
    </style>
    </head>
    <body>
    <title>Pico W HTTP Server</title>
    <h1>Pico W HTTP Server</h1>
    <h1>Toggle the LED with this button:</h1><br>

    <form accept-charset="utf-8" method="POST">{button}</form>
    <h1><p>Learn more at <A HREF="https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/overview">Adafruit</A>
    </h1>
    </body></html>
    """
    return html


server.serve_forever(str(wifi.radio.ipv4_address))

'''
    <p><form accept-charset="utf-8" method="POST">
    <button class="button" name="LED ON" value="ON" type="submit">LED ON</button></p>
    <button class="button" name="LED OFF" value="OFF" type="submit">LED OFF</button></p>
    <button class="button" name="move" value="forward" type="submit">FORWARD</button></a>
    <button class="button" name="move" value="backward" type="submit">BACKWARD</button></a>
    <label for="fname" style="font-size: 26px">Distance (mm):</label>
    <input type="text" id="distance" name="distance" class="resizedTextbox" style="font-size: 26px">

    </form>
    '''
