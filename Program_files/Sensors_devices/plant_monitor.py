from myDHT22 import DHT
from analog_calib import analogue_ada_sensor
from analog_calib import mapValue
import json
from plant import plant

##I am assuming that each device has its own DHT sensor

class plant_monitor(object):

    def __init__(self, name, device_id, dht_pin, dht_model, light_sensor_pin):
        self.name = name
        self.device_id = device_id
        self.dht_sensor = DHT(dht_pin, dht_model)
        self.light_sensor = analogue_ada_sensor("Light", light_sensor_pin)
        self.plants = [] 
        #self.analog_sensors = []
    
    ######Start of Getters########
    def get_device_name(self):
        return self.name
    
    def get_device_id(self):
        return self.device_id
    
    def get_temperature(self):
        return self.dht_sensor.get_temperature()
    
    def get_humidity(self):
        return self.dht_sensor.get_humidity()
    
    def get_light_value(self, min_measured, max_measured):
        light_percentage = self.light_sensor.get_mapped_value(min_measured, max_measured)
        return str(light_percentage) + "%" 
        
    #####End of Getters#######

    def add_analog_sensor(self, data_type, ads_pin):
        ada_sensor = analogue_ada_sensor(data_type, ads_pin)
        self.analog_sensors.append(ada_sensor)
    
    def add_plant(self, name, species, temperature_requirement, humidity_requirement, light_requirement, sensor_pin):
        p = plant(name, species, temperature_requirement, humidity_requirement, light_requirement, sensor_pin)
        self.plants.append(p)

    ## the minimum soil moisture value and max_soil_moisture values will be constant throughout.
    ## The user will have to calibrate their analogue sensors first.
    def get_results(self, min_soil_moisture, max_soil_moisture):
        results = {}

        for p in self.plants:
            results[p] = {
                "Temperature" : "{:1.1f}".format(self.get_temperature()), 
                "Humidity": "{:1.1f}".format(self.get_humidity()),
                p.get_soil_data_type(): p.get_soil_moisture(min_soil_moisture, max_soil_moisture),
                self.light_sensor.get_data_type(): str(self.get_light_value()) + "%"
                }
        return results
    
    ###format of the results
    ##{Plant Name: {Temperature:temp, Humidity: humid, light_exposure}}