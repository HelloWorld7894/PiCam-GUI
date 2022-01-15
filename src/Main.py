from tkinter import *

#Other imports
from PIL import ImageTk, Image
import Camera as C
import RPi.GPIO as GPIO
import os

"""
    MAIN WINDOW
"""
SaveDir = "/home/pi/CopernicusPi/src/saved/"
Selected_Items = []

class MainWin():
    def __init__(self, master):
        self.master = master
        self.master.attributes("-fullscreen", True)
        self.master.configure(bg="white")
        self.prev_inpt = 1
        self.InvokeInterrupt = 0

        Var = StringVar(self.master, "1")
        values = {"Photo ": "1",
                  "Camera Settings": "2",
                  "Image Processing": "3",
                  "Images": "4"}

        for Iter, (text, value) in enumerate ( values.items () ):
            Radiobutton (self.master, text=text, variable=Var,
                          value=value, indicator=0,
                          background="#0e86d1", height=3, width=15 ).grid ( row=Iter + 1, column=1 )

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

def Selection(var):
    Selected_Items.append(var)

def GetLocation(var, spec_win_parent):
    spec_win_parent.VariableOverride() #variable override
    C.CameraOFF()

    if int(var.get()) == 1: #Photograph mode
        Header = Label(spec_win_parent.master, text="Photograph mode", font=("Arial", 25), bg="white").grid(row=1, column=2)
        C.CameraON()
        spec_win_parent.ButtonCheck()

    elif int(var.get()) == 2: #Camera settings
        Header = Label(spec_win_parent.master, text="Camera settings", font=("Arial", 25), bg="white").grid(row=1, column=2)
        C.CameraON_preview()

        Selected_Items = []

        #brightness
        BrightScale = Scale ( spec_win_parent.master, label="brightness", from_=0, to=100, orient=HORIZONTAL,
                              length=150, showvalue=0, tickinterval=2, resolution=0.01,
                              command=Selection).grid(row=2, column=2)
        #sharpness
        SharpScale = Scale ( spec_win_parent.master, label="sharpness", from_=-100, to=100, orient=HORIZONTAL,
                              length=150, showvalue=0, tickinterval=2, resolution=0.01,
                              command=Selection).grid(row=3, column=2)
        #contrast
        ContrastScale = Scale ( spec_win_parent.master, label="contrast", from_=-100, to=100, orient=HORIZONTAL,
                              length=150, showvalue=0, tickinterval=2, resolution=0.01,
                              command=Selection).grid(row=4, column=2)
        #saturation
        SaturationScale = Scale ( spec_win_parent.master, label="saturation", from_=-100, to=100, orient=HORIZONTAL,
                              length=150, showvalue=0, tickinterval=2, resolution=0.01,
                              command=Selection).grid(row=5, column=2)
        #iso
        IsoScale = Scale ( spec_win_parent.master, label="ISO", from_=100, to=800, orient=HORIZONTAL,
                              length=150, showvalue=0, tickinterval=2, resolution=0.01,
                              command=Selection).grid(row=6, column=2)
        #exposure_compensation
        ExpCompScale = Scale ( spec_win_parent.master, label="exposure compensation", from_=-25, to=25, orient=HORIZONTAL,
                              length=150, showvalue=0, tickinterval=2, resolution=0.01,
                              command=Selection).grid(row=7, column=2)

        #TODO: Dodělat!
        #exposure_mode
        #meter_mode
        #awb_mode
        #resolution

        #Applying elements from selection
        C.Cam.brightness = Selected_Items[0]
        C.Cam.sharpness = Selected_Items[1]
        C.Cam.contrast = Selected_Items[2]
        C.Cam.saturation = Selected_Items[3]
        C.Cam.iso = Selected_Items[4]
        C.Cam.exposure_compensation = Selected_Items[5]

    elif int(var.get()) == 3: #Image processing
        Header = Label(spec_win_parent.master, text="Image processing", font=("Arial", 25), bg="white").grid(row=1, column=2)

        #NOT STILL DONE YET
        #TODO: Dodělat!
    elif int(var.get()) == 4: #Images
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
