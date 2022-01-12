#Imports
from picamera import PiCamera
import RPi.GPIO as GPIO
import os

#Camera setup
Cam = PiCamera(sensor_mode=2)

#Button setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)

#Basic Camera setup
Cam.brightness = 50
Cam.sharpness = 0
Cam.contrast = 0
Cam.saturation = 0
Cam.iso = 0
Cam.exposure_compensation = 0
Cam.exposure_mode = "auto"
Cam.meter_mode = "average"
Cam.awb_mode = "auto"
Cam.rotation = 180
Cam.hflip = False
Cam.vflip = False
Cam.crop = (0.0, 0.0, 1.0, 1.0)
Cam.framerate = 30

def CameraON():
    Cam.preview_fullscreen = False
    Cam.preview_window = (160, 80, 290, 220)
    Cam.resolution = (640, 480)
    Cam.start_preview()

def CameraOFF():
    Cam.stop_preview()

def ButtonCheck(spec_win, prev_inpt):
    inpt = GPIO.input(5)
    if ((not prev_inpt) and inpt):
        Folder_Len = len([name for name in os.listdir(".") if os.path.isfile(name)])
        Cam.capture("home/pi/Desktop/image" + str(Folder_Len) + ".jpg")

    spec_win.after(100, ButtonCheck(spec_win, inpt))
    #Folder_Len = len([name for name in os.listdir(".") if os.path.isfile(name)])
    #Cam.capture("home/pi/CopernicusPi/saved/image" + str(Folder_Len))

def CameraOFF():
    Cam.stop_preview()
