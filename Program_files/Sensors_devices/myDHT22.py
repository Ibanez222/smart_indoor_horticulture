import Adafruit_DHT
import time
import json
from datetime import datetime



class DHT(object):
    models = [Adafruit_DHT.DHT11, Adafruit_DHT.DHT22]
    
    def __init__(self, pin, model):
        self.pin = pin
        if model.lower() == "dht11":
            self.model = self.models[0]
        elif model.lower() == "dht22":
            self.model = self.models[1]
        else:
            raise ValueError("Please type in a right DHT sensor model!")
    
    def get_pin(self):
        return self.pin
    
    def get_model(self):
        return self.model

    '''
    def get_results(self): #This method returns a tuple which contains the (humidity, temp) readings
        return Adafruit_DHT.read_retry(self.model, self.pin)
'''
    def get_results(self):
         humidity, temperature = Adafruit_DHT.read_retry(self.model, self.pin)
         if humidity is not None and temperature is not None:
              return humidity, temperature
         else:
              raise RuntimeError("Failed to retrieve data from the sensor.")
        
    def get_humidity(self):
        return self.get_results()[0]
    
    def get_temperature(self):
        return self.get_results()[1]

    def __str__(self):
        return f"DHT Sensor (Model: {self.model.__name__}, Pin: {self.pin})"



sensor = DHT(4, "DHT22")
'''
sensor = DHT(4, Adafruit_DHT.DHT22)	

while True:
	humidity, temperature = sensor.get_results()
	timestamp = datetime.now()
	if humidity is not None and temperature is not None:
		#print("Temp = {0:0.1f}*C Humidity = {1:0.1f}%".format(temperature, humidity))
		data = {"timestamp": str(timestamp), "temperature": str(temperature), "Humidity": str(humidity)}
		print(json.dumps(data))
		time.sleep(10)
	else:
		print("Sensor failure. Check wiring.")
		time.sleep(3)
'''
