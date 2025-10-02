import machine
import utime
import urandom

# Set up LED, button and buzzer
led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(2, machine.Pin.OUT)

# Global variables
timer_start = 0

# Interrupt handler
def button_handler(pin):
    button.irq(handler=None)  # turn off trigger, so it's used only once
    reaction_time = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print("Your reaction time was " + str(reaction_time) + " milliseconds")
    print("Program complete.")

# Signal user to get ready
led.value(1)
utime.sleep(urandom.uniform(5, 10))  # random seconds between 5 and 10

# Turn off LED and give buzzer signal
led.value(0)
buzzer.value(1)
utime.sleep(0.2)   # short beep
buzzer.value(0)

# Start timer after signal
timer_start = utime.ticks_ms()

# Enable interrupt
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
