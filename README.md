# Hand_Geasture_Car_Control_Using_Open-CV

This Repo Can be used to control a RC car using Hand Gestures and ESP8266

Python version 3.8.10 , esptool version 2.8.

Initialy install thonny and micro-python in esp8266 using the firmware
https://micropython.org/download/esp8266/

Clone the repo, open ESP folder
Open connection.py add your credentials in the program to set connection with wifi
Now, open subsribe.py add your wifi ip address and set the speed limit as you wish.
Don't edit main.py
Open esp8266 file you will find boot.py in it edit it and just add "import main" as shown in my boot.py

Now connect save all this files in ESP8266

ESP8266 is ready 

Now connect your esp8266 with motor driver L293D as shown in image

install mosquitto using the txt file provided

Open hand.py add your wifi address and run 

opencv(4.6.0),cvzone(1.5.6),mediapipe(0.9.0),paho-mqtt(1.6.1),mosquitto(1.6.9)
