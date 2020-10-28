import pyautogui
import time
import win32api,win32con
# pyautogui.displayMousePosition()

def move(x,y):
    win32api.SetCursorPos((x,y))

# THIS CODE IS GOOD
##for i in range(10000000):
##        if pyautogui.pixel(820,410)[0] == 252:
##            pyautogui.moveTo(818,500)
##            
##        if pyautogui.pixel(965,410)[0] == 252:
##            pyautogui.moveTo(965,500)
##
##            
##        if pyautogui.pixel(1085,410)[0] == 252:
##            pyautogui.moveTo(1085,500)



    
# THIS CODE IS VERY GOOD    
##for i in range(10000000):
##        if pyautogui.pixel(820,415)[0] == 252:
##            pyautogui.moveTo(818,500)
##            
##        if pyautogui.pixel(965,415)[0] == 252:
##            pyautogui.moveTo(965,500)
##
##            
##        if pyautogui.pixel(1085,415)[0] == 252:
##            pyautogui.moveTo(1085,500)



for i in range(100000000000):
        if pyautogui.pixel(835,445)[0] == 252:
                move(823,500)    
            
        if pyautogui.pixel(975,445)[0] == 252:
                move(965,500)   

            
        if pyautogui.pixel(1105,455)[0] == 252:
                move(1085,500)
                       


    
