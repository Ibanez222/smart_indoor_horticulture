#from Sensors_devices.plant_monitor import plant_monitor
from Sensors_devices.analog_calib import analogue_ada_sensor
from Sensors_devices.analog_calib import get_control_value
import time
import json

#new_device = plant_monitor("Raspberry Pi", "Some Random Id", 4, "DHT22", 0)

#plant_monitor.add_plant("Lettuce", "Lettuce Family", 19.0, 50, 60, 1)

Sensor1 = analogue_ada_sensor("Soil Moisture", 1)
Sensor2 = analogue_ada_sensor("Soil Moisture", 2)
Sensor3 = analogue_ada_sensor("Soil Moisture", 3)

#time 1 minute

print(f"Sensor1: {get_control_value(Sensor1, 60)}")
      
print(f"Sensor2: {get_control_value(Sensor2, 60)}")
print(f"Sensor3: {get_control_value(Sensor3, 60)}")


##getting dry soil values

'''
while True:
    print("Sensor1 value: " + str(Sensor1.get_raw_value()) + "\tSensor2 value: " + str(Sensor2.get_raw_value())")
    time.sleep(0.5)
'''