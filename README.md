# CopernicusPi

a simple camera software developed in python-tkinter for Raspberry Pi with RPi HQ camera

## Installation

### Clone the repo
```
git clone https://github.com/HelloWorld7894/CopernicusPi.git
```

### Modify the lightdm.conf file to hide cursor (optional)
this command disables cursor! don´t use if you don´t have touchscreen attached to pi!
```
sudo nano /etc/lightdm/lightdm.conf
xserver-command = X -nocursor #add into file
```
### Install required frameworks
```
pip3 install Pillow, picamera
```

### Install required packages
```
sudo apt install tix-dev
```

## Run

just run the `python3 Main.py`, file can be found in /CopernicusPi/src/
