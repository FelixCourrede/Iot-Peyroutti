import paho.mqtt.client as mqtt
import datetime
from datetime import datetime as dt
import time
from time import sleep

t=round(time.time())
Whitelist=['04317f52da2c80']
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("fx4431@gmail.com/badger")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global Whitelist
    global t
    print(str(msg.payload.hex()))
    id=msg.payload.hex()
    tprime=round(time.time())
    if (tprime-t>1):
        if (id in Whitelist):
            reponse(1)
            t=round(time.time())
        else:
            reponse(0)
            t=round(time.time())

def reponse(valeurReponse):
    client = mqtt.Client()
    client.username_pw_set(username="fx4431@gmail.com",password="badger")
    client.on_connect = on_connect
    client.connect("maqiatto.com", 1883, 60)
    client.publish("fx4431@gmail.com/reponse",valeurReponse)


client = mqtt.Client()
client.username_pw_set(username="fx4431@gmail.com",password="badger")
client.on_connect = on_connect
client.on_message = on_message

client.connect("maqiatto.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()