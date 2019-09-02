#!/usr/bin/python3
from time import time, sleep
from tkinter import *
from picamera import PiCamera

camera = PiCamera()

class rearViewCam:

    def __init__(self, master):
        self.master = master

        self.labelText = StringVar()
        self.labelText.set("Cam Status")
        self.camStatus = Label(master, textvariable=self.labelText)
        self.camStatus.grid(row=2,columnspan=3)

        self.startButton = Button(master, text="Start Cam", command=self.startCam)
        self.startButton.grid(row=1,column=1)

        self.stopButton = Button(master, text="Stop Cam", state=DISABLED, command=self.stopCam)
        self.stopButton.grid(row=1,column=2)

    def startCam(self):
        self.labelText.set("Running")
        self.stopButton.config(state=NORMAL)
        
        camera.resolution = (1024, 768)
        camera.start_preview(fullscreen = False,
                             window = (190,40,510,350))

    def stopCam(self):
        if self.startCam is not None:
            self.startf = None
            camera.stop_preview()
            self.labelText.set("Stopped")
 


