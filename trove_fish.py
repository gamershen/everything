import pyautogui
import keyboard
import time


def boot_drop():
    drops = 0
    boot = pyautogui.locateCenterOnScreen("C:\\Users\\User\\Desktop\\python screenshots\\boot.png")
    trash = pyautogui.locateCenterOnScreen("C:\\Users\\User\\Desktop\\python screenshots\\trash.png")
    if boot != None:
        pyautogui.moveTo(1141,451)
        pyautogui.click()
        pyautogui.moveTo(boot[0],boot[1])
        pyautogui.click(button='middle')
        pyautogui.moveTo(trash[0]- 200,trash[1] - 300)
        pyautogui.click()
        drops += 1
    else:
        print(f"boots dropped until now: {drops}")



print("adjust window size..\nchoose mode:\n[1] change windows\n[2] one window")

x = input()
if x == "1":
    print('Bot Started')
    for i in range(5000000):
        pyautogui.moveTo(699,79)
        pyautogui.click()
        boot_drop()
        pyautogui.moveTo(65,796)
        pyautogui.click()
        boot_drop()
        pyautogui.moveTo(1635,893)
        pyautogui.click()
        boot_drop()
if x == "2":
    for i in range(50000):
        boot_drop()

        


