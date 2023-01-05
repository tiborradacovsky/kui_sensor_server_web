import time, network
from machine import Pin
import dht
import json
import urequests

SSID = "..."
PASSWORD = "..."
ROOM_ID = "100"
URL = "http://192.168.25.160:5000/sensor"

def measure_dht():
    sensor = dht.DHT11(Pin(14))
    sensor.measure()
    temp = sensor.temperature()
    # print("Temperature: ", temp)
    # humi = sensor.humidity()
    return temp


def make_connection():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("Connecting to SSID", SSID)
    # wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print('.')
        wlan.connect(SSID, PASSWORD)
        time.sleep(5)

    print(wlan.ifconfig())
    return True


def send_http_post_request(temperature_value):
    data = {
        "room_id": ROOM_ID,
        "temperature": temperature_value,
        "author": "Tibor"
    }
    print(data)
    url = URL
    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }
    urequests.post(url, data=json.dumps(data), headers=headers)

    return "Sent"


make_connection()
while True:
    print("Ziskavam teplotu")
    t = measure_dht()

    print("Odosielam teplotu")
    odpoved = send_http_post_request(t)
    print(odpoved)

    time.sleep(10)
