from buildhat import Motor, Matrix, ColorSensor, ForceSensor
from time import sleep

motor = Motor("D")
button = ForceSensor('B')
LED = Matrix('A')
LED.clear()
cs = ColorSensor('C')
print('start')
while True:
    button.wait_until_pressed(100)

    motor.run_for_degrees(90, blocking=True) #4 colours
   # motor.run_for_degrees(45, blocking=True, speed = 8) #8 colours
    sleep(0.5)
    c = cs.get_color()
    print(c)

    if c != 'black':
        LED.clear((c,10))
