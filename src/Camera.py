#Imports
from picamera import PiCamera

#Camera setup
Cam = PiCamera(sensor_mode=2)

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
Cam.rotation = 90
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

def CameraOFF():
    Cam.stop_preview()
