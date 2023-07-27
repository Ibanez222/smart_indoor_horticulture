from Sensors_devices.plant_monitor import plant_monitor
from Sensors_devices.crops import Plant

import time
import json

dry_sensor1_reading = 15968
wet_sensor1_reading = 8432
dry_sensor2_reading = 15636
wet_sensor2_reading = 8416
dry_sensor3_reading = 17536
wet_sensor3_reading = 12776

raspberry_pi = plant_monitor("RaspberryPi", "", 4, "DHT22", 0)
raspberry_pi.add_plant("Lettuce1", "Lettuce", 18.0, 75.0, 70, 1, wet_sensor1_reading, dry_sensor1_reading)
raspberry_pi.add_plant("Lettuce2", "Lettuce", 18.0, 75.0, 70, 2, wet_sensor3_reading, dry_sensor2_reading)
raspberry_pi.add_plant("Lettuce3", "Lettuce", 18.0, 75.0, 70, 3, wet_sensor3_reading, dry_sensor3_reading)


while True:
    print(json.dumps(raspberry_pi.get_results(), indent = 2))
    time.sleep(3)
