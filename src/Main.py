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
    MainWin.attributes("-fullscreen", True)
    MainWin.configure(bg="white")

LoadingWin = Tk(className="CopernicusPi-loader")
LoadingWin.configure(bg="white")

Logo = Canvas(LoadingWin, width=150, height=150)
Logo.pack()

Img = Image.open("./gui/CopernicusPi.png")
Resized_Img = Img.resize((150, 150))
Img_Canvas = ImageTk.PhotoImage(Resized_Img)
Logo.create_image(0, 0, anchor=NW, image=Img_Canvas)

LoadingWin.attributes("-fullscreen", True)
LoadingWin.after(3000, main)

# Execute tkinter
mainloop()
