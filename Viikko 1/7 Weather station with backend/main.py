import network
import time
import urequests
import dht
from machine import Pin, I2C

# Wi-Fi asetukset
SSID = 'Wokwi-GUEST'
PASSWORD = ''

# ThingSpeak API
THINGSPEAK_API_KEY = 'IQ6SWHKSC63ZT3ND'
THINGSPEAK_URL = 'http://api.thingspeak.com/update'

# DHT22 sensori (GP15)
sensor = dht.DHT22(Pin(15))

# LCD
I2C_ADDR = 0x27  # yleisin, joskus 0x3F
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

LCD_BACKLIGHT = 0x08
ENABLE = 0b00000100

def lcd_strobe(data):
    i2c.writeto(I2C_ADDR, bytearray([data | ENABLE | LCD_BACKLIGHT]))
    time.sleep_us(500)
    i2c.writeto(I2C_ADDR, bytearray([(data & ~ENABLE) | LCD_BACKLIGHT]))
    time.sleep_us(100)

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
    time.sleep_ms(50)
    lcd_cmd(0x33)
    lcd_cmd(0x32)
    lcd_cmd(0x28)
    lcd_cmd(0x0C)
    lcd_cmd(0x06)
    lcd_cmd(0x01)
    time.sleep_ms(5)

def lcd_clear():
    lcd_cmd(0x01)
    time.sleep_ms(5)

def lcd_puts(text, line=0):
    addr = 0x80 if line == 0 else 0xC0
    lcd_cmd(addr)
    for ch in text:
        lcd_char(ch)

# Alusta LCD
lcd_init()
lcd_puts("Connecting WiFi", 0)

# Wi-Fi yhteys
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(0.5)

lcd_clear()
lcd_puts("WiFi Connected", 0)
print("IP:", wlan.ifconfig()[0])
time.sleep(1)

def send_to_thingspeak(temp, hum):
    try:
        response = urequests.post(
            THINGSPEAK_URL,
            data='api_key={}&field1={}&field2={}'.format(THINGSPEAK_API_KEY, temp, hum),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        response.close()
        return True
    except Exception as e:
        print("Failed to send:", e)
        return False

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")

        sent = send_to_thingspeak(temperature, humidity)

        lcd_clear()
        lcd_puts("Temp:{:.1f}C".format(temperature), 0)
        if sent:
            lcd_puts("WiFi OK / Sent", 1)
        else:
            lcd_puts("Send Error", 1)

    except Exception as e:
        print("Error:", e)
        lcd_clear()
        lcd_puts("Sensor Error", 0)

    time.sleep(15)
