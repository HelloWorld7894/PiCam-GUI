from tkinter import *

#Other imports
from PIL import ImageTk, Image
import Camera as C
import RPi.GPIO as GPIO
import os

"""
    MAIN WINDOW
"""
def GetLocation(var, spec_win):
    #variable override
    for widget in spec_win.winfo_children():
        if "radiobutton" not in str(widget):
            widget.destroy()
    C.CameraOFF()

    if int(var.get()) == 1: #Photograph mode
        Header = Label(spec_win, text="Photograph mode", font=("Arial", 25), bg="white").grid(row=1, column=2)
        C.CameraON()

        prev_inpt = 1
        C.ButtonCheck(spec_win, prev_inpt)

    elif int(var.get()) == 2: #Camera settings
        Header = Label(spec_win, text="Camera settings", font=("Arial", 25), bg="white").grid(row=1, column=2)
    elif int(var.get()) == 3: #Image processing
        Header = Label(spec_win, text="Image processing", font=("Arial", 25), bg="white").grid(row=1, column=2)
    elif int(var.get()) == 4: #Images
        Header = Label(spec_win, text="Images", font=("Arial", 25), bg="white").grid(row=1, column=2)

def ButtonCheck(spec_win, prev_inpt):
    inpt = GPIO.input(5)
    if ((not prev_inpt) and inpt):
        Folder_Len = len([name for name in os.listdir(".") if os.path.isfile(name)])
        C.Cam.capture("home/pi/Desktop/image" + str(Folder_Len) + ".jpg")

    spec_win.after(100, ButtonCheck(spec_win, inpt))
    #Folder_Len = len([name for name in os.listdir(".") if os.path.isfile(name)])
    #Cam.capture("home/pi/CopernicusPi/saved/image" + str(Folder_Len))

def main():
    # destroy splash window
    LoadingWin.destroy()

    # Execute tkinter
    MainWin = Tk(className="CopernicusPi-main")

    # Adjust size
    MainWin.attributes("-fullscreen", True)
    MainWin.configure(bg="white")

    Var = StringVar(MainWin, "1")
    values = {"Photo ": "1",
              "Camera Settings": "2",
              "Image Processing": "3",
              "Images": "4"}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for Iter, (text, value) in enumerate(values.items()):
        Radiobutton ( MainWin, text=text, variable=Var,
                      value=value, indicator=0,
                      background="#0e86d1", height = 3, width = 15).grid(row= Iter + 1, column=1)

    GetLocation(Var, MainWin)
    Var.trace("w", lambda *_, VarInstnc=Var: GetLocation(VarInstnc, MainWin))

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
