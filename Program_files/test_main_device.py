from Sensors_devices.plant_monitor import plant_monitor
import time
import json

new_device = plant_monitor("Raspberry Pi", "Some Random Id", 4, "DHT22", 0)

plant_monitor.add_plant("Lettuce", "Lettuce Family", 19.0, 50, 60, 1)

