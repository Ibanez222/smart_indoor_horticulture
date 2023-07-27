from Sensors_devices.analog_calib import analogue_ada_sensor
from Sensors_devices.analog_calib import get_control_value
import time
import json
import csv

#new_device = plant_monitor("Raspberry Pi", "Some Random Id", 4, "DHT22", 0)

#plant_monitor.add_plant("Lettuce", "Lettuce Family", 19.0, 50, 60, 1)

Sensor1 = analogue_ada_sensor("Soil Moisture", 1)
Sensor2 = analogue_ada_sensor("Soil Moisture", 2)
Sensor3 = analogue_ada_sensor("Soil Moisture", 3)

count = 0
'''
with open('wet_value_soil_moisture_s3_t2.csv', 'w', newline='') as file:
        write_soil = csv.writer(file)
        write_soil.writerow(["Wet Reading"] + ["Time(s)"])

        while count < 60:
                print("Reading s3: " + str(Sensor3.get_raw_value()))
                write_soil.writerow([str(Sensor3.get_raw_value())] + [str(count)])
                time.sleep(1)
                count += 1
'''
#while count < 60:


##getting dry soil values

while True:
    print("Sensor1 value: " + str(Sensor1.get_raw_value()) + "\tSensor2 value: " + str(Sensor2.get_raw_value()))
    time.sleep(0.5)
