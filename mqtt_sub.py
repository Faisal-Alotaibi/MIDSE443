import time
import paho.mqtt.client as paho
import json


# broker = "localhost"
broker = "10.20.1.95"

#broker="iot.eclipse.org"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    y = json.loads(str(message.payload.decode("utf-8")))
    print("studentid = ", y["studentid"]) 
    print("name = ", y["name"]) 
    print("surname = ", y["surname"]) 
    print("telephone = ", y["telephone"]) 
    print("grade = ", y["grade"]) 
    



client= paho.Client() 
client.on_message = on_message
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("se443/midterm2")#subscribe
while(True):
	client.on_message=on_message
