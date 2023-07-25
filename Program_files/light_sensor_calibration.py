#from Sensors_devices.plant_monitor import plant_monitor
from Sensors_devices.analog_calib import analogue_ada_sensor
from Sensors_devices.analog_calib import get_control_value
import time
import json

#new_device = plant_monitor("Raspberry Pi", "Some Random Id", 4, "DHT22", 0)

#plant_monitor.add_plant("Lettuce", "Lettuce Family", 19.0, 50, 60, 1)

LDR = analogue_ada_sensor("Light Levels", 0)

#time 1 minute

print(f"LDR: {get_control_value(LDR, 20)}")

##getting dry soil values

'''
while True:
    print("Sensor1 value: " + str(Sensor1.get_raw_value()) + "\tSensor2 value: " + str(Sensor2.get_raw_value())")
    time.sleep(0.5)
'''