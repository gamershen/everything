import pyautogui
import time
import random
import keyboard
import msvcrt


pyautogui.size()

# press g to stop


pyautogui.moveTo(1059,586)

def clicker(i):
    for i in range(1,i):
        pyautogui.click()
        if keyboard.is_pressed('g'):
            break



clicker(100000000)
