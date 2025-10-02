import machine
import utime

led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(2, machine.Pin.OUT)

I2C_ADDR = 0x27
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=400000)

LCD_BACKLIGHT = 0x08
ENABLE = 0b00000100

def lcd_strobe(data):
    i2c.writeto(I2C_ADDR, bytearray([data | ENABLE | LCD_BACKLIGHT]))
    utime.sleep_us(500)
    i2c.writeto(I2C_ADDR, bytearray([(data & ~ENABLE) | LCD_BACKLIGHT]))
    utime.sleep_us(100)

def lcd_write(data, mode=0):
    high = data & 0xF0
    low = (data << 4) & 0xF0
    for d in (high, low):
        i2c.writeto(I2C_ADDR, bytearray([d | mode | LCD_BACKLIGHT]))
        lcd_strobe(d | mode)

def lcd_cmd(cmd):
    lcd_write(cmd, 0)

def lcd_char(char):
    lcd_write(ord(char), 1)

def lcd_init():
    utime.sleep_ms(50)
    lcd_cmd(0x33)
    lcd_cmd(0x32)
    lcd_cmd(0x28)
    lcd_cmd(0x0C)
    lcd_cmd(0x06)
    lcd_cmd(0x01)
    utime.sleep_ms(5)

def lcd_clear():
    lcd_cmd(0x01)
    utime.sleep_ms(5)

def lcd_puts(text, line=0):
    addr = 0x80 if line == 0 else 0xC0
    lcd_cmd(addr)
    for ch in text:
        lcd_char(ch)

lcd_init()
lcd_puts("Traffic Lights", 0)
lcd_puts("Ready...", 1)
utime.sleep(2)

# Pääohjelma
while True:
    if button.value() == 1:
        led_red.value(1)
        lcd_clear()
        lcd_puts("Button Pressed", 0)
        lcd_puts("STOP!", 1)
        for i in range(5):
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        led_red.value(0)

    # Punainen
    led_red.value(1)
    lcd_clear()
    lcd_puts("LIGHT:", 0)
    lcd_puts("RED", 1)
    utime.sleep(2)
    led_red.value(0)

    # Keltainen
    led_yellow.value(1)
    lcd_clear()
    lcd_puts("LIGHT:", 0)
    lcd_puts("YELLOW", 1)
    utime.sleep(2)
    led_yellow.value(0)

    # Vihreä
    led_green.value(1)
    lcd_clear()
    lcd_puts("LIGHT:", 0)
    lcd_puts("GREEN", 1)
    utime.sleep(2)
    led_green.value(0)
