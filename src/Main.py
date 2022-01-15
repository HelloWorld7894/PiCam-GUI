from tkinter import *
from tkinter.tix import *

#Other imports
from PIL import ImageTk, Image
import Camera as C
import RPi.GPIO as GPIO
import os

"""
    MAIN WINDOW
"""
SaveDir = "/home/pi/CopernicusPi/src/saved/"
# set to default variables
Camera_Settings = [50, #brightness
                   0, #sharpness
                   0, #contrast
                   0, #saturation
                   0, #iso
                   0, #exposure compensation
                   1000, #shutter speed (default)
                   "auto", #exposure mode
                   "average", #meter mode
                   "auto", #awb mode
                   90, #rotation (default always)
                   False, #hflip (default always)
                   False, #vflip (default always)
                   (0.0, 0.0, 1.0, 1.0), #crop (default always)
                   30 #framerate
                   #TODO: Add resolution!!!
                   ]
C.Load_Settings(Camera_Settings) #Default load

#values for settings 1
BrightnessVal = SharpnessVal = ContrastVal = SaturationVal = DoubleVar()
#values for settings 2
IsoVar = Exposure_compensationVal = ShutterSpeedVal = DoubleVar()
ExposureVar = "auto"
#values for settings 3
MeterVar, AwbVar = "average", "auto"
#TODO: Dodělat i resolution

class MainWin():
    def __init__(self, master):
        self.master = master
        self.master.attributes("-fullscreen", True)
        self.master.configure(bg="white")
        self.prev_inpt = 1
        self.InvokeInterrupt = 0

        Var = StringVar(self.master, "1")
        values = {"Photo ": "1",
                  "Camera Setting 1": "2",
                  "Camera Setting 2": "3",
                  "Camera Setting 3": "4",
                  "Image Processing": "5",
                  "Images": "6"}

        for Iter, (text, value) in enumerate ( values.items () ):
            Radiobutton (self.master, text=text, variable=Var,
                          value=value, indicator=0,
                          background="#0e86d1", height=3, width=13).grid ( row=Iter + 1, column=1)

        GetLocation(Var, self)
        Var.trace("w", lambda *_, VarInstnc=Var: GetLocation(VarInstnc, self))

    def ButtonCheck(self):
        inpt = GPIO.input(5)
        if ((not self.prev_inpt) and inpt):
            Folder_Len = 0
            for File in os.listdir(SaveDir):
                if os.path.isfile(SaveDir + File): Folder_Len += 1
            C.Cam.capture(SaveDir + str(Folder_Len) + ".jpg" )

        self.prev_inpt = inpt

        self.master.after(100, self.ButtonCheck)

    def VariableOverride(self):
        for widget in self.master.winfo_children():
            if "radiobutton" not in str(widget):
                widget.destroy()

    def ViewFile(self, Spec_Path):
        self.VariableOverride() #variable override

        ViewWin = Tk(Spec_Path)
        View_File = Image.open(Spec_Path)
        View_File_resized = View_File.resize((300, 300))

        Label(ViewWin, image = View_File_resized).pack()

        ViewWin.mainloop()

def Get_and_Load():
    Data = [BrightnessVal, SharpnessVal, ContrastVal, SaturationVal, IsoVar,
            Exposure_compensationVal, ShutterSpeedVal, ExposureVar, MeterVar, AwbVar,
            90, False, False, (0.0, 0.0, 1.0, 1.0), 30] #Default parameters
            #TODO: Add resolution!
    C.Load_Settings(Data)

def GetLocation(var, spec_win_parent):
    spec_win_parent.VariableOverride() #variable override
    C.CameraOFF()

    if int(var.get()) == 1: #Photograph mode
        Header = Label(spec_win_parent.master, text="Photograph mode", font=("Arial", 25), bg="white").grid(row=1, column=2)
        C.CameraON()
        spec_win_parent.ButtonCheck()

    elif int(var.get()) == 2: #Camera setting 1
        Header = Label(spec_win_parent.master, text="Camera settings", font=("Arial", 25), bg="white").grid(row=1, column=2)
        C.CameraON_preview()

        #brightness
        BrightScale = Scale(spec_win_parent.master, label="brightness", from_=0, to=100, orient=HORIZONTAL,
                              length=110, showvalue=0, tickinterval=2, resolution=0.01,
                              variable=BrightnessVal).grid(row=2, column=2, padx=0)
        #sharpness
        SharpScale = Scale(spec_win_parent.master, label="sharpness", from_=-100, to=100, orient=HORIZONTAL,
                              length=110, showvalue=0, tickinterval=2, resolution=0.01,
                              variable=SharpnessVal).grid(row=3, column=2, padx=0)
        #contrast
        ContrastScale = Scale(spec_win_parent.master, label="contrast", from_=-100, to=100, orient=HORIZONTAL,
                              length=110, showvalue=0, tickinterval=2, resolution=0.01,
                              variable=ContrastVal).grid(row=4, column=2, padx=0)
        #saturation
        SaturationScale = Scale(spec_win_parent.master, label="saturation", from_=-100, to=100, orient=HORIZONTAL,
                              length=110, showvalue=0, tickinterval=2, resolution=0.01,
                              variable=SaturationVal).grid(row=5, column=2, padx=0)

        Save = Button(spec_win_parent.master, text="Save", command=Get_and_Load).grid(row=6, column=3)

    elif int(var.get()) == 3: #Camera setting 2
        Header = Label ( spec_win_parent.master, text="Camera settings", font=("Arial", 25), bg="white" ).grid(row=1, column=2)
        C.CameraON_preview()

        # iso
        IsoScale = Scale ( spec_win_parent.master, label="ISO", from_=100, to=800, orient=HORIZONTAL,
                           length=110, showvalue=0, tickinterval=2, resolution=0.01,
                           variable=IsoVar).grid ( row=2, column=2, padx=0 )
        # exposure_compensation
        ExpCompScale = Scale ( spec_win_parent.master, label="exposure compensation", from_=-25, to=25,
                               orient=HORIZONTAL,
                               length=110, showvalue=0, tickinterval=2, resolution=0.01,
                               variable=Exposure_compensationVal).grid(row=3, column=2, padx=0)
        # shutter_speed
        ShutterSpeedScale = Scale(spec_win_parent.master, label="shutter speed", from_=200, to=6000000,
                                  orient=HORIZONTAL,
                                  length=110, showvalue=0, tickinterval=2, resolution=0.01,
                                  variable=ShutterSpeedVal).grid(row=4, column=2, padx=0)

        #Variable resetting
        ExposureVar = StringVar(spec_win_parent.master, "1")

        # exposure_mode
        ExposureMode_Values = {"auto": "1",
                               "off": "2",
                               "night": "3",
                               "backlight": "4",
                               "sports": "5",
                               "snow": "6",
                               "beach": "7",
                               "verylong": "8",
                               "antishake": "9"}
        for Iter, (text, value) in enumerate(ExposureMode_Values.items()):
            Radiobutton(spec_win_parent.master, text=text, variable=ExposureVar,
                        value=value, indicator=0,
                        background="#0e86d1", height=2, width=3).grid(row=5, column=Iter + 1)

        Save = Button(spec_win_parent.master, text="Save", command=Get_and_Load).grid(row=8, column=3)

    elif int(var.get()) == 4: #Camera Setting 3
        Header = Label ( spec_win_parent.master, text="Camera settings", font=("Arial", 25), bg="white" ).grid(row=1, column=2 )
        C.CameraON_preview()

        #Variable resetting
        MeterVar, AwbVar = StringVar(spec_win_parent.master, "1")

        # meter_mode
        MeterMode_Values = {"average": "1",
                            "spot": "2",
                            "backlit": "3",
                            "matrix": "4"}
        for Iter, (text, value) in enumerate(MeterMode_Values.items()):
            Radiobutton(spec_win_parent.master, text=text, variable=MeterVar,
                        value=value, indicator=0,
                        background="#0e86d1", height=2, width=3).grid(row=1, column=Iter + 1)
        # awb_mode
        AwbMode_Values = {"off": "1",
                          "auto": "2",
                          "sunlight": "3",
                          "cloudy": "4",
                          "shade": "5",
                          "tungsten": "6",
                          "fluor": "7",
                          "incan": "8",
                          "flash": "9",
                          "horizon": "10"}
        for Iter, (text, value) in enumerate(AwbMode_Values.items()):
            Radiobutton(spec_win_parent.master, text=text, variable=AwbVar,
                        value=value, indicator=0,
                        background="#0e86d1", height=2, width=3).grid(row=2, column=Iter + 1)
        # resolution
        #TODO: Dodělat!

        Save = Button(spec_win_parent.master, text="Save", command=Get_and_Load ).grid (row=4, column=3)

    elif int(var.get()) == 5: #Image processing
        Header = Label(spec_win_parent.master, text="Image processing", font=("Arial", 25), bg="white").grid(row=1, column=2)

        #NOT STILL DONE YET
    elif int(var.get()) == 6: #Images
        Header = Label(spec_win_parent.master, text="Images", font=("Arial", 25), bg="white").grid(row=1, column=2)

        Folder_Len = 0
        for File in os.listdir ( SaveDir ):
            if os.path.isfile ( SaveDir + File ): Folder_Len += 1

        if Folder_Len == 0:
            Info = Label(spec_win_parent.master, text="No Images found", bg="white").grid(row=2, column=2)
        else:
            #NOT STILL DONE YET
            # TODO: Dodělat!
            for File in os.listdir ( SaveDir ):
                if os.path.isfile ( SaveDir + File ):
                    pass



def main():
    # destroy splash window
    LoadingWin.destroy()

    # Execute tkinter
    Global_Win = MainWin(Tk(className="CopernicusPi-main"))

#Button setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)

LoadingWin = Tk(className="CopernicusPi-loader")
LoadingWin.configure(bg="white")

Logo = Canvas(LoadingWin, width=300, height=300)
Logo.pack()

Img = Image.open("./gui/CopernicusPi.png")
Resized_Img = Img.resize((300, 300))
Img_Canvas = ImageTk.PhotoImage(Resized_Img)
Logo.create_image(0, 0, anchor=NW, image=Img_Canvas)

LoadingWin.attributes("-fullscreen", True)
LoadingWin.after(3000, main)

# Execute tkinter
mainloop()
