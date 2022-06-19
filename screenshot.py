from pynput import mouse
from PIL import ImageGrab
import datetime
import time

def click(x, y, button, pressed):
    if x >= 1000 and y <= 500:
        now = datetime.datetime.now()
        ImageGrab.grab().save("{}.png".format(now.strftime("%Y-%m-%d %H-%M-%S")))
        print("clicked on ({}, {})".format(x, y))
        time.sleep(3)

mouse_listener = mouse.Listener(on_click=click)

mouse_listener.start()
