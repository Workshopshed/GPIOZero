from gpiozero import Button

DIP = (Button(6), Button(5), Button(25), Button(24), Button(23), Button(22), Button(27), Button(17))

total = 0
bit = 1

for switch in DIP:
    if (switch.value):
        total += bit
    bit *= 2

print (total)
