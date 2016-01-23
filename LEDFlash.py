from gpiozero import LED
from time import sleep

green = 12

led = LED(green)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
