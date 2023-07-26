from Sensors_devices.plant_monitor import plant_monitor
from Sensors_devices.crops import Plant

import time

dry_sensor1 = 8814
dry_sensor2 = 8754
dry_sensor3 = 13008

wet_sensor1 = 6418
wet_sensor2 = 6232
wet_sensor3 = 9427

raspberry_pi = plant_monitor("RaspberryPi", "connection_string", 4, "DHT22", 0)
raspberry_pi.add_plant("Lettuce1", "Lettuce", 18.0, 50.0, 70, 1, wet_sensor1, dry_sensor1)
raspberry_pi.add_plant("Lettuce2", "Lettuce", 18.0, 50.0, 70, 2, wet_sensor2, dry_sensor2)
raspberry_pi.add_plant("Lettuce3", "Lettuce", 18.0, 50.0, 70, 3, wet_sensor3, dry_sensor3)
 

while True:
    print(raspberry_pi.get_results())
    time.sleep(3)