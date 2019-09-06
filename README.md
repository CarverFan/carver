# carver
Python GPS Speedometer &amp; Camera Control

Simple Python3 Tkinter application that displays a GPS powered speedometer and some buttons for controlling the Raspberry Pi Camera module.

The speedometer gauge code (gaugelib.py) was written by Ardiotech.com 

I've written this to be integrated with the OpenAuto Pro application but it does work standalone using the hardware listed below:

Raspberry Pi 3 B+
Official 7 Inch Touch Screen
Raspberry Pi Camera Module V2
USB GPS Module

OpenAuto Pro comes bundled in it's own Raspian ISO so your installation path's may not match those below.

INSTALLATION

Add the speedo.py app to the OpenAuto Pro Appliciations list, I've added mine at the beginning of the list:

pi@raspberrypi:~ $ head openauto_applications.ini
[Applications]
Count=6

[Application_0]
Name=Speedo
Path=sudo python3 /usr/local/bin/speedo.py
IconPath=/home/pi/icons/icon_speedo.png
Autostart=true
~

Then copy all three project files into the /usr/local/bin folder.  Change their ownership and make them executable:

sudo chown root:staff speedo.py

sudo chown root:staff rvcamlib.py

sudo chown root:staff gaugelib.py


sudo chmod +x speedo.py

sudo chmod +x rvcamlib.py

sudo chmod +x gaugelib.py

You'll want to edit the rvcamlib.py file and change the recording location variable 'vidpath'.

You can test by running from the command line:

sudo python3 speedo.py




