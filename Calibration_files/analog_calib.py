import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#This is assuming the user has enabled the i2c bus in the raspberry pi 3's configuration
#Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
digital_converter = ADS.ADS1015(i2c)

print(type(digital_converter))
#this class will work if the platform/raspberry pi 3 is using an Adafruit ads1x15 analog - digital converter
class analogue_ada_sensor(object):
    channel = None
    def __init__(self, signal_converter, pin):
        self.signal_converter = signal_converter
        self.channel = AnalogIn(signal_converter, pin) #The channel value will be ADS.PX (P0-P3)
    
    def get_signal_converter(self):
        return self.signal_coverter
    
    def get_channel(self):
        return self.channel
    
    def get_voltage(self):
        return self.channel.voltage
    
    def get_raw_value(self):
        return self.channel.value
    
##calibrating the sensor
##recommended that there is an open air and wet control value
def get_mean_control_value(sensor, Time): #argument must be the analogue_ada_sensor type and the seconds
    control_values = []
    
    for i in range(Time):
        sensor_value = sensor.get_raw_value()
        control_values.append(sensor_value)
        print(f"raw data value: {sensor_value}")
        time.sleep(1) #get reading per second
    
    total = 0
    
    for reading in control_values:
        total += reading
       
    return total/len(control_values)

##based on arduino map() function
def mapValue(sensor_value, min_value, max_value, mappedLow, mappedHigh):
        return ((sensor_value - min_value) * (mappedHigh - mappedLow)) / (max_value - min_value) + mappedLow


###testing




