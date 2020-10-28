import cv2 as cv
import numpy as np
import pyautogui
import time
from PIL import Image
import keyboard
import random
import win32api,win32con

##pyautogui.displayMousePosition()

    
for i in range(1000):
    for g in range(729,1194):
        if pyautogui.pixel(g,520)[0] > 230 and pyautogui.pixel(g,520)[1] > 200:
            pyautogui.moveTo(g,499)
    

