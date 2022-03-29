from picamera import PiCamera

# Camera setup
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


def Load_Settings(Settings):
    setting_keys = ["brightness", "sharpness", "contrast", "saturation",
                    "iso", "exposure_compensation", "shutter_speed",
                    "exposure_mode", "meter_mode", "awb_mode", "rotation",
                    "hflip", "vflip", "crop", "framerate"]

    for setting in setting_keys:
        setattr(Cam, setting, Settings[setting])
