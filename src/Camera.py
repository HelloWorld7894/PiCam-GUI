#Imports
from picamera import PiCamera

#Camera setup
Cam = PiCamera(sensor_mode=2)

def CameraON():
    Cam.preview_fullscreen = False
    Cam.preview_window = (160, 80, 290, 220)
    Cam.resolution = (640, 480)
    Cam.start_preview()

def CameraON_preview():
    Cam.preview_fullscreen = False
    Cam.preview_window = (300, 40, 200, 200)
    Cam.resolution = (640, 480)
    Cam.start_preview()

def CameraOFF():
    Cam.stop_preview()

def CameraOFF():
    Cam.stop_preview()

def Load_Settings(Settings):
    Cam.brightness = Settings[0]
    Cam.sharpness = Settings[1]
    Cam.contrast = Settings[2]
    Cam.saturation = Settings[3]
    Cam.iso = Settings[4]
    Cam.exposure_compensation = Settings[5]
    Cam.exposure_mode = Settings[6]
    Cam.meter_mode = Settings[7]
    Cam.awb_mode = Settings[8]
    Cam.rotation = Settings[9]
    Cam.hflip = Settings[10]
    Cam.vflip = Settings[11]
    Cam.crop = Settings[12]
    Cam.framerate = Settings[13]