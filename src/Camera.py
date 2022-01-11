#Imports
from picamera import PiCamera
from gpiozero import Button #I tried manually with GPIO module, but the signal outputting was broken
import os

#Camera setup
Cam = PiCamera(sensor_mode=2)

#Button setup
Button_instance = Button(5) #GPIO on pi 5

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
Cam.rotation = 0
Cam.hflip = False
Cam.vflip = False
Cam.crop = (0.0, 0.0, 1.0, 1.0)
Cam.framerate = 30

def CameraON():
    Cam.preview_fullscreen = False
    Cam.preview_window = (160, 80, 290, 220)
    Cam.resolution = (640, 480)
    Cam.start_preview()

    Button_instance.wait_for_press()

    Folder_Len = len([name for name in os.listdir(".") if os.path.isfile(name)])
    Cam.capture("home/pi/CopernicusPi/saved/image" + Folder_Len)

def CameraOFF():
    Cam.stop_preview()