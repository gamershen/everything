import pyautogui



def buy():
    pyautogui.moveTo(721,135)
    pyautogui.click()

    for i in range(500000):
        resell = pyautogui.locateCenterOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\resell.png')
        yes = pyautogui.locateCenterOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\Yes.png')

        if resell != None:
            pyautogui.moveTo(resell[0],resell[1])
            pyautogui.click()
            pyautogui.moveTo(yes[0],yes[1])
            pyautogui.click()

        else:
            continue



x = input('adjust window size\npress enter when ready')
        
if x == "":
    buy()
