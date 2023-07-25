from Sensors_devices.plant_monitor import plant_monitor
from Sensors_devices.crops import Plant

import time

raspberry_pi = plant_monitor("RaspberryPi", "connection_string", 4, "DHT22", 0)

while True:
    print(raspberry_pi.get_temperature())
    time.sleep(3)