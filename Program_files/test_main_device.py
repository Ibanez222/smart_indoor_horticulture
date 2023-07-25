from Sensors_devices.plant_monitor import plant_monitor
from Sensors_devices.analog_calib import analogue_ada_sensor
import Sensors_devices.analog_calib
import time
import json

#new_device = plant_monitor("Raspberry Pi", "Some Random Id", 4, "DHT22", 0)

#plant_monitor.add_plant("Lettuce", "Lettuce Family", 19.0, 50, 60, 1)

Sensor1 = analogue_ada_sensor("Soil Moisture", 1)
Sensor2 = analogue_ada_sensor("Soil Moisture", 2)
Sensor3 = analogue_ada_sensor("Soil Moisture", 3)

while True:
    print("Sensor1 value: " + Sensor1.get_raw_value() )
    print("Sensor2 value: " + Sensor1.get_raw_value() )
    print("Sensor3 value: " + Sensor1.get_raw_value() )    