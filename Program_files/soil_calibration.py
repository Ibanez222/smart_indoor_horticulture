#from Sensors_devices.plant_monitor import plant_monitor
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

with open('Normal_readings.csv', 'w', newline='') as file:
	write_soil = csv.writer(file)
	write_soil.writerow(["Normal Reading"] + ["Control Material: Soil/Compost"])
	write_soil.writerow(["Time"] + ["Sensor1"] + ["Sensor2"] + ["Sensor3"] + ["Voltage"])
	
	while count < 60:
		print("Reading s1: " + str(Sensor1.get_raw_value()) + ", Reading s2: " + str(Sensor2.get_raw_value()) + ", Reading s3: " + str(Sensor3.get_raw_value()))
		write_soil.writerow([str(count + 1)] + [str(Sensor1.get_raw_value())] + [str(Sensor1.get_voltage())] + [str(Sensor2.get_raw_value())] + [str(Sensor2.get_voltage())] + [str(Sensor3.get_raw_value())] + [str(Sensor3.get_voltage())])
		time.sleep(1)
		count += 1

#while count < 60:


##getting dry soil values

'''
while True:
    print("Sensor1 value: " + str(Sensor1.get_raw_value()) + "\tSensor2 value: " + str(Sensor2.get_raw_value())")
    time.sleep(0.5)
'''
