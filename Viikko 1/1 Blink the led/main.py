import machine
import time
time.sleep(0.1)

led_onboard = machine.Pin(15, machine.Pin.OUT)

while True:
    # lyhyt välähdys
    led_onboard.value(1)
    time.sleep(0.2)
    led_onboard.value(0)
    time.sleep(0.2)

    # pitkä välähdys
    led_onboard.value(1)
    time.sleep(0.8)
    led_onboard.value(0)
    time.sleep(0.8)
