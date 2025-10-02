import machine
import time
import dht

# Initialize DHT22 sensor on GPIO15
sensor = dht.DHT22(machine.Pin(15))

# LEDs
red_led = machine.Pin(2, machine.Pin.OUT)   # temperature warning
blue_led = machine.Pin(4, machine.Pin.OUT)  # humidity warning

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature: {:.1f}°C".format(temperature))
        print("Humidity: {:.1f}%".format(humidity))

        # Temperature alarm
        if temperature > 30:
            red_led.value(1)
        else:
            red_led.value(0)

        # Humidity alarm
        if humidity < 30:
            blue_led.value(1)
        else:
            blue_led.value(0)

    except OSError as e:
        print("Sensor read error:", e)

    time.sleep(2)
