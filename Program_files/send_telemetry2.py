import time
import json
from datetime import datetime

from Sensors_devices.plant_monitor import plant_monitor
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=IOTGarden.azure-devices.net;DeviceId=raspberryPi;SharedAccessKey=46CRN2+Bvvozcjil3POL7vJdh/tjy4ZnRth1oyG4utg="


raspberry_pi = plant_monitor("RaspberryPi", CONNECTION_STRING, 4, "DHT22", 0)
raspberry_pi.add_plant("Lettuce1", "Lettuce", 18.0, 75.0, 70, 1, 4672, 11568)
raspberry_pi.add_plant("Lettuce2", "Lettuce", 18.0, 75.0, 70, 2, 6192, 13648)
raspberry_pi.add_plant("Lettuce3", "Lettuce", 18.0, 75.0, 70, 3, 7904, 14048)

def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(raspberry_pi.get_device_id)
    return client

def iot_client_telemetry_sample_run():
    
    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        while True:
            # Get sensor_device Data 
#            humidity, temperature = sensor_device.get_results()
            temperature = raspberry_pi.get_temperature()

            message = Message(raspberry_pi.get_results())

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if temperature > 20:
              message.custom_properties["temperatureAlert"] = "true"
            else:
              message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(3)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()


