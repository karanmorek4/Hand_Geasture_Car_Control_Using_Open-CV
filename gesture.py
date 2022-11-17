import cv2
import paho.mqtt.client as mqtt
import time

from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.75,maxHands=1)

cap=cv2.VideoCapture(0)
count=0

ipaddr = "192.168.43.102"

def one():
    global ipaddr
    mqttBroker =ipaddr
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("NULL",(bytes("one",'utf-8')))     

def two():
    global ipaddr
    mqttBroker =ipaddr
    client = mqtt.Client("raspberry pi 401")
    client.connect(mqttBroker)
    client.publish("NULL",(bytes("two",'utf-8')))     

def three():
    global ipaddr
    mqttBroker =ipaddr
    client = mqtt.Client("raspberry pi 401")
    client.connect(mqttBroker)
    client.publish("NULL",(bytes("three",'utf-8')))    

def four():
    global ipaddr
    mqttBroker =ipaddr
    client = mqtt.Client("raspberry pi 401")
    client.connect(mqttBroker)
    client.publish("NULL",(bytes("four",'utf-8')))  

def stop():
    global ipaddr
    mqttBroker =ipaddr
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("NULL",(bytes("stop",'utf-8')))     

while True:
    
    ret,frame=cap.read()
    
    count += 1
    if count % 14 != 0:
        continue
    
    hands,frame=detector.findHands(frame)
    
    if not hands:
        stop()
    else: 
        hands1=hands[0]
        bbox=hands1["bbox"]
        x,y,w,h=bbox
        fingers1=detector.fingersUp(hands1)
        count = fingers1.count(1)
        print('Count of 1:', count)
        if count==1:
            one()
        elif count==2:
             two()
        elif count==3:
            three()
        elif count==4:
            four()
        elif count==5:
            stop()

    frame=cv2.imshow("Image",frame)
   
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
