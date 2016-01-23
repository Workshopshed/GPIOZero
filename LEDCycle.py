from gpiozero import LED
from time import sleep

green = LED(12)
red = LED(13)
yellow = LED(19)

while True:
    yellow.off()
    green.on()
    sleep(1)
    green.off()
    red.on()
    sleep(1)
    red.off()
    yellow.on()
    sleep(1)
