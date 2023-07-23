from typing import Any


class plant(object):
    def __init__(self, name, species, temperature_requirement, humidity_requirement, light_requirement):
        self.name = name
        self.species = species
        self.temperature_requirement = temperature_requirement
        self.humidity_requirement = humidity_requirement
        self.light_requirement = light_requirement

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
    
