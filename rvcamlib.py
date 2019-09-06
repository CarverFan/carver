#!/usr/bin/python3
from time import time, sleep
from tkinter import *
from picamera import PiCamera
from datetime import datetime, date, timedelta

camera = PiCamera()

vidpath = '/media/usb/video/'

class rearViewCam:

    def __init__(self, master):
        self.master = master
        self.button_clicks = 0

        self.labelText = StringVar()
        self.labelText.set("Cam Status Off")
        self.camStatus = Label(master, textvariable=self.labelText)
        self.camStatus.grid(row=2,columnspan=3)

        self.startButton = Button(master, text="Start", command=self.startCam)
        self.startButton.grid(row=1,column=0)

        self.stopButton = Button(master, text="Stop", state=DISABLED, command=self.stopCam)
        self.stopButton.grid(row=1,column=1)

        self.recButton = Button(master, text="Record", fg="green", command=self.recCam)
        self.recButton.grid(row=1,column=2)

    def startCam(self):
        self.labelText.set("Running")
        self.stopButton.config(state=NORMAL)
        
        camera.resolution = (1024, 768)
        camera.start_preview(fullscreen = False,
                             window = (185,25,510,350))

    def stopCam(self):
        if self.startCam is not None:
            self.startf = None
            camera.stop_preview()
            self.labelText.set("Stopped") 

    def recCam(self):
        self.button_clicks += 0
        self.labelText.set("Recording ")
        self.recButton['text'] = "Start"
        if self.button_clicks == 0:
            self.button_clicks += 1
            self.recButton['text'] = "Started"
            self.recButton['fg'] = "red"
            # start recording
            now = datetime.now()
            dtStr = now.strftime("%d%m%Y-%H%M%S")
            vidfile = vidpath + "vid-" + dtStr + ".h264"
            camera.resolution = (1024, 768)
            camera.start_recording(vidfile)
        else:
            self.labelText.set("Stopped Recording")
            self.recButton['text'] = "Record"
            self.recButton['fg'] = "green"
            # stop recording
            camera.stop_recording()
            self.button_clicks = 0
           



