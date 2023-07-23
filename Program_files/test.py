##Testing the DHT sensor
from Sensors_devices.myDHT22 import DHT

myDHT = DHT(4, "DHT22")

while True:
    
    humidity, temperature = myDHT.get_results()
    print("Temperature = {:1.1f}*C".format(temperature) + " Humidity = {:1.1f}%".format(humidity))
