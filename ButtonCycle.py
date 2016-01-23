from gpiozero import LED, Button

button = Button(18)

green = LED(12)
red = LED(13)
yellow = LED(19)

while True:
    yellow.off()
    green.on()
    button.wait_for_press()
    button.wait_for_release()
    green.off()
    red.on()
    button.wait_for_press()
    button.wait_for_release()
    red.off()
    yellow.on()
    button.wait_for_press()
    button.wait_for_release()
