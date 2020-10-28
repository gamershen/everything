import pyautogui
import time
import win32api,win32con
import keyboard
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
##pyautogui.displayMousePosition()
##if pyautogui.pixel(958,y)[0]

def melee():
    time.sleep(1)
    for i in range(100000000):
        if keyboard.is_pressed('q'):
            break
        shell.SendKeys("{left}")
        time.sleep(0.1)
        shell.SendKeys("{right}")
        time.sleep(0.1)
        shell.SendKeys("{up}")
        time.sleep(0.1)


def magic():
    time.sleep(2)
    for i in range(50000000):
       pyautogui.moveTo(783,450,duration = 0.2)
       pyautogui.moveTo(1231,450,duration = 0.2)
       pyautogui.moveTo(783,520,duration = 0.2)
       pyautogui.moveTo(1231,520,duration = 0.2)
       pyautogui.moveTo(783,650,duration = 0.2)
       pyautogui.moveTo(1231,650,duration = 0.2)
    



def agility():
    for i in range(500000000):
        if pyautogui.pixel(1049,551)[0] != 166:
            shell.SendKeys("{down}")
            time.sleep(0.6)
        if pyautogui.pixel(1067,620)[0] != 152:
            shell.SendKeys("{up}")
            time.sleep(0.6)
        if pyautogui.pixel(1230,522)[0] != 137:
            shell.SendKeys("{left}")
            time.sleep(0.6)
        if pyautogui.pixel(855,620)[0] != 147:
            shell.SendKeys("{up}")
            time.sleep(0.6)
        if pyautogui.pixel(850,551)[0] != 157:
            shell.SendKeys("{down}")
            time.sleep(0.6)
        if pyautogui.pixel(685,513)[0] != 122:
            shell.SendKeys("{right}")
            time.sleep(0.6)
    
melee()
