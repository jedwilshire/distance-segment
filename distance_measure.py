from board import I2C
from time import sleep
from adafruit_ht16k33.segments import Seg7x4
from gpiozero import Button, DistanceSensor
b = Button('BOARD33')
ds = DistanceSensor(echo = 'BOARD32', trigger = 'BOARD36')
i2c = I2C()
disp = Seg7x4(i2c, address = 0x70)
while not b.is_pressed:
    # program loop
    dist = round(ds.distance * 100, 1)
    disp.fill(0)
    disp.print(str(dist))
    sleep(0.5)
# end program
disp.fill(0)


