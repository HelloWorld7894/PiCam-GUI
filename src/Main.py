from tkinter import *
from tkinter.ttk import *

#Other imports
from PIL import ImageTk, Image

"""
    MAIN WINDOW
"""
def main():
    # destroy splash window
    LoadingWin.destroy()

    # Execute tkinter
    MainWin = Tk(className="CopernicusPi-main")

    # Adjust size
    MainWin.geometry("400x400")
    MainWin.attributes("-fullscreen", True)
    MainWin.configure(bg="white")

LoadingWin = Tk(className="CopernicusPi-loader")
LoadingWin.geometry("200x200")
LoadingWin.configure(bg="white")

Logo = Canvas(LoadingWin, width=500, height=500)
Logo.pack()

Img = ImageTk.PhotoImage(Image.open("./gui/CopernicusPi.png"))
Logo.create_image(0, 0, anchor=NW, image=Img)

LoadingWin.attributes("-fullscreen", True)
LoadingWin.after(3000, main)

# Execute tkinter
mainloop()
