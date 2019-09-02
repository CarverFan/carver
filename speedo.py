#!/usr/bin/python3

from tkinter import *
#import tkinter as tk
#from tkinter.font import Font
#from tkinter import messagebox
from time import time, sleep
import random
import gaugelib
import serial
from picamera import PiCamera
import rvcamlib

gps = serial.Serial("/dev/ttyACM1", baudrate = 9600)

win = Tk()
#a5 = PhotoImage(file="g1.png")
#win.tk.call('wm', 'iconphoto', win._w, a5)
win.title("Speed")
win.geometry("200x320+0+0")
win.resizable(width=False, height=False)
win.configure(bg='black')
runWindow = rvcamlib.rearViewCam(win)

g_value=0
x=0
course="0"

def read_every_second():
    global x
    global g_value_mph
    global course
    #g_value=random.randint(0,70)
    line = gps.readline().decode("utf-8")
    data = line.split(",")

    if data[0] == "$GNVTG":
        # km/h
        g_value = float(data[7])
        # mph
        g_value_mph = (g_value / 1.609)

        
        courseEmptyTest = data[1]
        print("cempty: %s" % (courseEmptyTest))

        if courseEmptyTest == '':
           course = 0
        else:
           course = float(data[1])

        if course == 0:
           courseText = 'North'
        elif 1 <= course <= 44:
           courseText = 'NNE'
        elif course == 45:
           courseText = 'NE'
        elif 46 <= course <= 89:
           courseText = 'ENE'
        elif course == 90:
           courseText = 'East'
        elif 91 <= course <= 134:
           courseText = 'ESE'
        elif course == 135:
           courseText = 'SE'
        elif 136 <= course <= 179:
           courseText = 'SSE'
        elif course == 180:
           courseText = 'South'
        elif 181 <= course <= 224:
           courseText = 'SSW'
        elif course == 225:
           courseText = 'SW'
        elif 226 <= course <= 269:
           courseText = 'WSW'
        elif course == 270:
           courseText = 'West'
        elif 271 <= course <= 314:
           courseText = 'WNW'
        elif course == 315:
           courseText = 'NW'
        elif 316 <= course <= 359:
           courseText = 'NNW'
        else:
           courseText = '???'

        p1.set_value(int(g_value_mph), str(courseText))

        print("mph: %.2f, course: %s" % (g_value_mph, courseText))
        print("VTG: %s" % (data))

    if data[0] == "$GNRMC":
       #print("RMC: %s" % (data))
       if data[2] == "A":

          dateTime = str(data[9]) + str(data[1])
          latgps = float(data[3])
          if data[4] == "S":
              latgps = -latgps

          latdeg = int(latgps/100)
          latmin = latgps - latdeg*100
          lat = latdeg+(latmin/60)

          longps = float(data[5])
          if data[6] == "W":
              longps = -longps

          londeg = int(longps/100)
          lonmin = longps - londeg*100
          lon = londeg+(lonmin/60)

          direction = data[8]
      
          with open("/media/usb/gps/gps-data-" + str(data[9]) + ".log", "a+") as pos: 
              pos.write("Lat: %s, Lon: %s, dt: %s\n" % (lat, lon, dateTime))
              if 'g_value_mph' in globals():
                  pos.write("mph: %.2f, Direction: %s\n" % (g_value_mph, direction))


    x+=1
    if x>100:
        #graph1.draw_axes()
        x=0
    win.after(100, read_every_second)

p1 = gaugelib.DrawGauge2(
    win,
    max_value=100.0,
    min_value=0.0,
    size=200,
    bg_col='black',
    unit = "SPEED", unit1="HEADING", bg_sel = 2)

p1.grid(row=0, columnspan=3)

read_every_second()
mainloop()
