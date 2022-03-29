# CopernicusPi

![Could not load CopernicusPi logo](https://github.com/HelloWorld7894/CopernicusPi/blob/main/src/gui/CopernicusPi.png?raw=true)

A simple camera software developed in `python-tkinter` for Raspberry Pi with RPi HQ camera.

## Installation

### Clone the repo
```sh
git clone https://github.com/HelloWorld7894/CopernicusPi.git
```

### Install required frameworks
```sh
pip3 install Pillow, picamera
```

### Install required packages
```sh
sudo apt install tix-dev
```

### Modify the lightdm.conf file to hide cursor (optional)
This command disables cursor! Don´t use if you don´t have touchscreen attached to pi!
```sh
sudoedit /etc/lightdm/lightdm.conf
# Add this to the file:
# xserver-command = X -nocursor
```

## Run
```sh
./src/Main.py
```
