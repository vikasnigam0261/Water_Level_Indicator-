import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "7jh6o2",
        "typeId": "VITDevice",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    water_level=random.randint(1,100)
    light_intensity=random.randint(0,100)
    myData={'Water_Level':water_level, 'Light_Intensity':light_intensity}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("VIKAS KUMAR NIGAM:::Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
