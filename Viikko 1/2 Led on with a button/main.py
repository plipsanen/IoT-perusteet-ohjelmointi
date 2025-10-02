import machine
import time

led = machine.Pin(18, machine.Pin.OUT)
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

led.value(0)

while True:
    if button.value() == 0:   # nappia painetaan
        led.toggle()
        time.sleep(0.1)       # vilkkuu nopeasti
    else:
        led.value(0)          # sammuu kokonaan
