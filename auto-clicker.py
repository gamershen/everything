import pyautogui
import time
import win32api,win32con
import keyboard

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

start = input("set up a start button: ")
stop = input("set up a stop button: ")


def clicking(stop,start):
    print(f"program started\npress {stop} to stop")
    while True:
        click()
        if keyboard.is_pressed(stop):
           while True:
               if keyboard.is_pressed(start):
                   break
        continue

  
print(f"start: {start}, stop: {stop}\nset up your mouse and press {start} to start")

while True:
    if keyboard.is_pressed(start):
        clicking(stop,start)
