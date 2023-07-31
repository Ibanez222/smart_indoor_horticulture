from Sensors_devices.myDHT22 import DHT
from Sensors_devices.analog_calib import analogue_ada_sensor
from Sensors_devices.analog_calib import mapValue
import json
from Sensors_devices.crops import Plant

##I am assuming that each device has its own DHT sensor

class plant_monitor(object):

    min_light_value = 6816
    max_light_value = 23344
    
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
    
    def get_light_value(self):
        light_percentage = None
        
        if(self.light_sensor.get_raw_value() <= self.min_light_value):
            light_percentage = 0
        elif(self.light_sensor.get_raw_value() >= self.max_light_value):
            light_percentage = 100
        else:
            light_percentage = self.light_sensor.get_mapped_value(self.min_light_value, self.max_light_value)

        return light_percentage 
    
    def get_plants_list(self):
        return self.plants
    #####End of Getters#######
    '''
    def add_analog_sensor(self, data_type, ads_pin):
        ada_sensor = analogue_ada_sensor(data_type, ads_pin)
        self.analog_sensors.append(ada_sensor)
    '''
    def add_plant(self, name, species, temperature_requirement, humidity_requirement, light_requirement, sensor_pin, wet_value, dryvalue):
        p = Plant(name, species, temperature_requirement, humidity_requirement, light_requirement, sensor_pin, wet_value, dryvalue)
        self.plants.append(p)
    
    ####Checks in the code#######
    def temp_check(self, veg): ##Plant classes only
        responses = ["Too Cold", "Colder Temperature", "Optimal Temperature", "Warmer Growing Temperature", "Too Hot"]
        temp_requirement = veg.get_temp_variable()
        tolerance = 5  # Tolerance for checking temperature ranges. Assuming 5C is the range for each categories 
    
        # Define temperature ranges based on the temperature requirement
        min_temp = temp_requirement - tolerance
        max_temp = temp_requirement + tolerance
        warmer_temp = temp_requirement + 5 + tolerance

        temp_reading = self.get_temperature()

        if temp_reading > warmer_temp:
            return responses[4]
        elif temp_reading >= max_temp:
            return responses[3]
        elif temp_reading <= min_temp:
            return responses[1]
        elif min_temp < temp_reading < max_temp:
            return responses[2]
        else:
            return "Unknown"
    
    
    def hum_check(self, veg):
        responses = ["Low Humidity", "Optimum Humidity Met", "Hgh Humidity"]
        hum_requirement = veg.get_hum_variable()
        hum_reading = self.get_humidity()
        tolerance = 25
        
        max_humidity = hum_requirement
        min_humidity = hum_requirement - tolerance
        
        if hum_reading > max_humidity:
            return responses[2]
        elif hum_reading >= min_humidity:
            return responses[1]
        else:
            return responses[0]
    
    def soil_moisture_check(self, veg):
        responses = ["No Watering needed", "Needs More Water"]
        soil_moisture_reading = veg.get_soil_moisture()
        
        if soil_moisture_reading > 50:
            return responses[0]
        elif soil_moisture_reading > 0:
            return responses[1]
        
    def check_light(self, veg):
        
        light_reading = self.get_light_value()
        
        if light_reading > 90:
            return "Direct Sun"
        elif light_reading > 80:
            return "Slightly Cloudy"
        elif light_reading > 60:
            return "Cloudy"
        elif light_reading > 0:
            return "Rain"
        else:
            return "Night Time"
        
        
        
    
    ## the minimum soil moisture value and max_soil_moisture values will be constant throughout.
    ## The user will have to calibrate their analogue sensors first.
    def get_results(self):
        results = []

        for p in self.plants:
            temp_reading = self.get_temperature()
            humidity = self.get_humidity()
            light_reading = self.get_light_value()
            all_results = {
                "Plant Name" : p.get_plant_name(),
                "Device Name": self.get_device_name(),
                "Temperature" : temp_reading, 
                "Humidity": humidity,
                p.get_soil_data_type(): p.get_soil_moisture(),
                self.light_sensor.get_data_type():  light_reading,
                "Temperature Check": self.temp_check(p),
                "Humidity Check": self.hum_check(p),
                "Sun Exposure Check": self.check_light(p),
                "Soil Moisture Check": self.soil_moisture_check(p)
                }
            
            results.append(all_results)

        return results
    
    ###format of the results
    ##{Plant Name: {Temperature:temp, Humidity: humid, light_exposure}}
