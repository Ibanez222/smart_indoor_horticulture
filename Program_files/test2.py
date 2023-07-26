from Sensors_devices.analog_calib import analogue_ada_sensor
from Sensors_devices.analog_calib import get_control_value, mapValue
import time

light_sensor = analogue_ada_sensor("Light intensity", 0)

#readings = get_control_value(light_sensor, 10)

#print("The reading is: " + str(readings))


max_value = 23344
min_value = 6816

while True:
    print(str(light_sensor.get_mapped_value(min_value, max_value)) + "%")
    time.sleep(1)