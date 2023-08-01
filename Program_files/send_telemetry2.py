import time
import json
from datetime import datetime

from Sensors_devices.plant_monitor import plant_monitor
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=smart-indoor-horticulture.azure-devices.net;DeviceId=raspberrypi1;SharedAccessKey=EYtxrElRsc1WdP9FV/nO0VCJvO4+zxxVKygHKs2OG2M="
#CONNECTION_STRING = "HostName=RaspberryPiBackUp.azure-devices.net;DeviceId=planterpi;SharedAccessKey=leJP9WLH6XIDnQts+GsWKY3QMWY7iNDtY34Inu1H6JU="

dry_sensor1_reading = 15968
wet_sensor1_reading = 8432
dry_sensor2_reading = 15636
wet_sensor2_reading = 8416
dry_sensor3_reading = 17536
wet_sensor3_reading = 12776

raspberry_pi = plant_monitor("RaspberryPi", CONNECTION_STRING, 4, "DHT22", 0)
raspberry_pi.add_plant("Lettuce1", "Lettuce", 18.0, 75.0, 70, 1, wet_sensor1_reading, dry_sensor1_reading)
raspberry_pi.add_plant("Lettuce2", "Lettuce", 18.0, 75.0, 70, 2, wet_sensor2_reading, dry_sensor2_reading)
raspberry_pi.add_plant("Lettuce3", "Lettuce", 18.0, 75.0, 70, 3, wet_sensor3_reading, dry_sensor3_reading)

def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(raspberry_pi.get_device_id())
    return client

def iothub_client_telemetry_sample_run():
    
    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        while True:
            # Get sensor_device Data 
#            humidity, temperature = sensor_device.get_results()
            temperature = raspberry_pi.get_temperature()

            message = Message(json.dumps(raspberry_pi.get_results(), indent=2))

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
            time.sleep(600)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()


