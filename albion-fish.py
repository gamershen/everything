import pyautogui
import time
# pyautogui.displayMousePosition()
# X:  947 Y:  166 RGB: ( 87,  91, 126)


##pyautogui.moveTo(947,166)
##pyautogui.displayMousePosition()
##X: 1080 Y:  138

def throw():
    time.sleep(5)
    pyautogui.moveTo(1061,134)
    print("throwing bait")
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseUp()
    time.sleep(3)
    for i in range(50000000000):
        if pyautogui.pixel(1080,138)[0] < 100:
            pyautogui.click() # working
            print("caught fish")
            time.sleep(0.2)
            fish()# working
            time.sleep(1)
        else:
            continue

def fish():
    pyautogui.mouseDown()#1
    print("down")
    time.sleep(0.7)
    pyautogui.mouseUp()
    print("up")
    time.sleep(0.2)
    pyautogui.mouseDown()#2
    print("down 2")
    time.sleep(1)
    pyautogui.mouseUp()
    print("up")
    time.sleep(0.2)
    pyautogui.mouseDown()#3
    print("down 3")
    time.sleep(0.6)
    pyautogui.mouseUp()
    print("up")
    time.sleep(0.2)
    pyautogui.mouseDown()#4
    print("down 4")
    time.sleep(0.6)
    pyautogui.mouseUp()
    print("up")
    time.sleep(0.2)
    pyautogui.mouseDown()#5
    print("down 5")
    time.sleep(0.3)
    pyautogui.mouseUp()
    print("up")
    time.sleep(0.2)
    pyautogui.mouseDown()#6
    print("down 6")
    time.sleep(0.7)


##pyautogui.moveTo(947,166)
##pyautogui.displayMousePosition()



for i in range(50000000000):
    throw()
    time.sleep(1)
        
        

    
