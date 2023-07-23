from Sensors_devices.analog_calib import analogue_ada_sensor
from Sensors_devices.analog_calib import get_control_value, mapValue

light_sensor = analogue_ada_sensor("Light intensity", 0)

readings = get_control_value(light_sensor, 10)

print("The reading is: " + str(readings))
