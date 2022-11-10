from buildhat import Motor, Matrix, ColorSensor, ForceSensor # import all the LEGO devices
from time import sleep


LED = Matrix('A') # 3x3 LED matrix connected to Build HAt port A
button = ForceSensor('B') # Force sensor connected to Build HAt port B
cs = ColorSensor('C') # Colour sensor connected to Build HAt port C
motor = Motor("D") # Motor connected to Build HAt port D

LED.clear() # Turnn off any LED pixels that might be on

print('start')

while True:
    button.wait_until_pressed(100) # Wait for the button to be pressed

    motor.run_for_degrees(90, blocking=True) # 4 colours
   # motor.run_for_degrees(45, blocking=True, speed = 8) #8 colours
    sleep(0.5)
    c = cs.get_color() # Get colour reading from sensor
    print(c)

    if c != 'black':
        LED.clear((c,10)) # set all the LEDs to the detected colour
