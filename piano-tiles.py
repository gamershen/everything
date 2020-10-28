import pyautogui
import time
import win32api,win32con
import keyboard

##pyautogui.displayMousePosition()
##if pyautogui.pixel(820,415)[0] == 252:

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def hold(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
y = 460
g = y - 45
#song 7 : Beyer No.8
if pyautogui.pixel(958,y)[0] == 67:
    click(980,y)
        
if pyautogui.pixel(1042,y)[0] == 67:
    click(1077,y)
        
if pyautogui.pixel(1123,y)[0] == 67:
    click(1167,y)
        
if pyautogui.pixel(1206,y)[0] == 67:
    click(1236,y)
    

for i in range(1500): #10 million
    if pyautogui.pixel(958,y-130)[0] == 1:
       click(980,g)
        
    if pyautogui.pixel(1039,y-130)[0] == 1:
       click(1077,g)
        
    if pyautogui.pixel(1123,y-130)[0] == 1:
       click(1167,g)
        
    if pyautogui.pixel(1206,y-130)[0] == 1:
       click(1236,g)


    if pyautogui.pixel(958,y-130)[0] == 0:
       hold(980,g)
        
    if pyautogui.pixel(1039,y-130)[0] == 0:
       hold(1077,g)
        
    if pyautogui.pixel(1123,y-130)[0] == 0:
       hold(1167,g)
        
    if pyautogui.pixel(1206,y-130)[0] == 0:
       hold(1236,g)







