import pyautogui
import time

##pyautogui.moveTo(1120,551)
##pyautogui.click() # move to game
##time.sleep(3)
##
##pyautogui.moveTo(859,521)
##pyautogui.click() # enter game
##



def farm():
    pyautogui.moveTo(1120,551)
    pyautogui.click() # move to game
    time.sleep(3.5)

    pyautogui.moveTo(859,521)
    pyautogui.click() # enter game
    time.sleep(0.2)
    
    pyautogui.moveTo(983,799)
    pyautogui.click()
    time.sleep(0.3)
    
    for i in range(840):
        pyautogui.moveTo(327,886)
        pyautogui.moveTo(1580,886)
    pyautogui.moveTo(1559,202)
    pyautogui.click()
    


for i in range(5000):
    farm()
 
