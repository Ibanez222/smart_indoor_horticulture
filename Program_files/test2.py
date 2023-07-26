from Sensors_devices.analog_calib import analogue_ada_sensor
from Sensors_devices.analog_calib import get_control_value, mapValue
import time
import csv


light_sensor = analogue_ada_sensor("Light intensity", 0)

#readings = get_control_value(light_sensor, 10)

#print("The reading is: " + str(readings))
count = 0

with open('light_exposure_max.csv', 'w', newline = '') as file:
    write_values = csv.writer(file)

    write_values.writerow(['Max Readings'] + ['Time'])
    while count < 20:
        write_values.writerow([str(light_sensor.get_raw_value())] + [str(count)])    
        time.sleep(1)
        count += 1
'''
max_value = 23344
min_value = 6816

while True:
    print("{:1.1f}".format(light_sensor.get_mapped_value(min_value, max_value)) + "%")
    print("Reading: " + str(light_sensor.get_raw_value()))
    time.sleep(1)
'''
