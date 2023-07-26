from Sensors_devices.analog_calib import mapValue ## each plant for each raspberry pi contains a capacitive moisture sensor
from Sensors_devices.analog_calib import analogue_ada_sensor

class Plant(object):
    def __init__(self, name, species, min_temp_requirement, min_hum_requirement, min_light_requirement, soil_moist_pin, min_soil_cal, max_soil_cal):
        self.name = name
        self.species = species
        self.min_temp_requirement = min_temp_requirement
        self.min_hum_requirement = min_hum_requirement
        self.min_light_requirement = min_light_requirement
        self.cap_soil_moist_sensor = analogue_ada_sensor("Soil Moisture", soil_moist_pin)
        self.min_soil_cal = min_soil_cal
        self.max_soil_cal = max_soil_cal
    
    #######Getters Setters##################
    
    def get_plant_name(self):
        return self.name
    
    def set_temp_variable(self, temperature_requirement):
        self.temperature_requirement = temperature_requirement

    def get_temp_variable(self):
        return self.temperature_requirement
    
    def set_hum_variable(self, humidity_requirement):
        self.humidity_requirement = humidity_requirement

    def get_hum_variable(self):
        return self.humidity_requirement
    
    def set_light_variable(self, light_requirement):
        self.light_requirement = light_requirement

    def get_light_variable(self):
        return self.light_requirement
    
    ##This method will calibrate the raw soil moisture data
    def get_soil_moisture(self):
        return 100 - self.cap_soil_moist_sensor.get_mapped_value(self.min_soil_cal, self.max_soil_cal)
    
    def get_soil_data_type(self):
        return self.cap_soil_moist_sensor.get_data_type()

    def __str__(self):
        return f"Plant: {self.name} ({self.species})\nTemperature Requirement: {self.temperature_requirement} °C\nHumidity Requirement: {self.humidity_requirement}%\nLight Requirement: {self.light_requirement} Lux"
