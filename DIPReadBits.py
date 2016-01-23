from gpiozero import Button

DIP = (Button(6), Button(5), Button(25), Button(24), Button(23), Button(22), Button(27), Button(18), Button(17))

for switch in DIP:
    print (switch.value)
