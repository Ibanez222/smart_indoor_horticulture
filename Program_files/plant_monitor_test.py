from Sensors_devices.plant_monitor import plant_monitor
from Sensors_devices.crops import Plant

import time

raspberry_pi = plant_monitor("RaspberryPi", "connection_string", 4, "DHT22", 0)
raspberry_pi.add_plant("Lettuce", 18.0, 50.0, 70, 1, 4672, 11568)
raspberry_pi.add_plant("Lettuce", 18.0, 50.0, 70, 2, 6192, 13648)
raspberry_pi.add_plant("Lettuce", 18.0, 50.0, 70, 3, 7904, 14048)


while True:
    print(raspberry_pi.get_results())
    time.sleep(3)