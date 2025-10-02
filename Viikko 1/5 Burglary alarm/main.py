import machine
import utime

# PIR-anturi
sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Sisäinen LED
led = machine.Pin("LED", machine.Pin.OUT)

# Uusi ulkoinen punainen LED
red_led = machine.Pin(15, machine.Pin.OUT)

def pir_handler(pin):
    print("ALARM! Motion detected!")
    red_led.value(1)  # sytytä punainen LED
    for i in range(50):
        led.toggle()
        utime.sleep_ms(100)
    red_led.value(0)  # sammuta punainen LED

# Keskeytys kun PIR havaitsee liikettä
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
