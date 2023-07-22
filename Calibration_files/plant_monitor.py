from analog_calib import analogue_ada_sensor
from analog_calib import mapValue #to map analogue values
#from myDHT22 import DHT
import json
from plant import plant


class plant_monitor(object):
    def __init__(self, name, sensor_list = [], plant_list = []):
        self.name = name
        self.sensor_list = sensor_list
        self.plant_list = plant_list

    def get_name(self):
        return self.name
    
    def add_analogue_sensor(self, data_type, signal_converter, pin):
        analog_sensor = analogue_ada_sensor(data_type, signal_converter, pin)
        self.sensor_list.append(analog_sensor)

    def add_dht_sensor(self, pin, model): # Only two models required for input "DHT22" and "DHT11"
        dht = DHT(pin, model)
        self.sensor_list.append(dht)

    def add_plant(self, name, species, temp_requirement, hum_requirement, light_requirement):
        Plant = plant(name, species, temp_requirement, hum_requirement, light_requirement)
        self.plant_list.append(Plant)

    def get_sensor_data(self):
        pass

    def send_telemetry_data(self):
        pass