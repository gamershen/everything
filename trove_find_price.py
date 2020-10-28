import pyautogui
import time
import winsound

#pyautogui.screenshot('C:\\Users\\User\\Desktop\\python screenshots\\shapestone_price2.png')+
##price_2 = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\glim_price_2.png')
##price_2_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\shapestone_price_2..png')
##price_3 = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\shapestone_price_3.png')
##price_3_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\shapestone_price_3..png')
##price_4 = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\shapestone_price_4.png')
##price_60_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\nitro_price_60..png')
##price_70 = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\nitro_price_70.png')
##price_150_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\dust_price_150..png')
##price_160_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\dust_price_160..png')
##price_170_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\dust_price_170..png')
##price_100_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\dust_price_100..png')

search = pyautogui.locateCenterOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\search.png')
buy = pyautogui.locateCenterOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\buy.png')



##search
##pyautogui.moveTo(search[0],search[1])
##pyautogui.click()
##pyautogui.moveTo(search[0]+3,search[1]+3)



def buying():
    pyautogui.moveTo(buy[0]+360,buy[1]+15)
    pyautogui.click()
    pyautogui.moveTo(buy[0]+360,buy[1]+100)
    pyautogui.click()
    time.sleep(0.5)
        




    
def buy_shape():
    print("searching Shapestone Ore...")
    bought = 0
    search_bar = pyautogui.locateCenterOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\search_bar.png')
    pyautogui.moveTo(search_bar[0],search_bar[1])
    pyautogui.click()
    pyautogui.moveTo(search_bar[0]+5,search_bar[1])
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite('')
    pyautogui.typewrite('Shapestone Ore')
    
    

    
    for i in range(100000):
        search
        pyautogui.moveTo(search[0],search[1])
        pyautogui.click()
        pyautogui.moveTo(search[0]-400,search[1])
        pyautogui.click()
        pyautogui.moveTo(search[0],search[1]+50)
        pyautogui.click()

        price_4 = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\shapestone_price_4.png')

        if price_4 != None:
            print("found price, buying for 4 ea")
            buying()
            bought += 1

##        price_3_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\price_3..png')
##
##        if price_3_ != None:
##            print("found price, buying for 3 ea")
##            buying()
##            bought += 1
        else:
            print(f"price not found, bought: {bought}")
            continue
      



def buy_nitro():
    print("Nitro-Glitterine")
    bought = 0
    search_bar = pyautogui.locateCenterOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\search_bar.png')
    pyautogui.moveTo(search_bar[0],search_bar[1])
    pyautogui.click()
    pyautogui.moveTo(search_bar[0]+5,search_bar[1])
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite('')
    pyautogui.typewrite('Nitro-Glitterine')
    

    
    for i in range(100000):
        search
        pyautogui.moveTo(search[0],search[1])
        pyautogui.click()
        pyautogui.moveTo(search[0]-400,search[1])
        pyautogui.click()
        pyautogui.moveTo(search[0],search[1]+50)
        pyautogui.click()

        price_60_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\nitro_price_60..png')

        if price_60_ != None:
            print("found price, buying for 60 ea")
            buying()
            bought += 1
        
        else:
            print(f"price not found, bought: {bought}")
            continue





def buy_dust():
    print("searching Faerie Dust...")
    bought = 0
    search_bar = pyautogui.locateCenterOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\search_bar.png')
    pyautogui.moveTo(search_bar[0],search_bar[1])
    pyautogui.click()
    pyautogui.moveTo(search_bar[0]+5,search_bar[1])
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite('')
    pyautogui.typewrite('Faerie Dust')
    

    
    for i in range(100000):
        search
        pyautogui.moveTo(search[0],search[1])
        pyautogui.click()
        pyautogui.moveTo(search[0]-400,search[1])
        pyautogui.click()
        pyautogui.moveTo(search[0],search[1]+50)
        pyautogui.click()

        price_150 = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\dust_price_150..png')

        if price_100_ != None:
            print("found price, buying")
            buying()
            bought += 1
        
        else:
            print(f"price not found, bought: {bought}")
            continue




def buy_cinnabar():
    print("searching Cinnabar...")
    bought = 0
    search_bar = pyautogui.locateCenterOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\search_bar.png')
    pyautogui.moveTo(search_bar[0],search_bar[1])
    pyautogui.click()
    pyautogui.moveTo(search_bar[0]+5,search_bar[1])
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite('')
    pyautogui.typewrite('Cinnabar')
    

    
    for i in range(100000):
        search
        pyautogui.moveTo(search[0],search[1])
        pyautogui.click()
        pyautogui.moveTo(search[0]-400,search[1])
        pyautogui.click()
        pyautogui.moveTo(search[0],search[1]+50)
        pyautogui.click()

        price_20 = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\cinnabar_price_20.png')

        if price_20 != None:
            print("found price, buying for 20 ea")
            buying()
            bought += 1

        price_10_ = pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\python screenshots\\price_100..png')
        
        if price_10_ != None:
            print("found price, buying for 10 ea")
            buying()
            bought += 1
        
        else:
            print(f"price not found, bought: {bought}")
            continue


               
answer = input("what you want to search?\n[1] Shapestone Ore\n[2] Nitro-Glitterine\n[3] Faerie Dust\n[4] Cinnabar\n")

if answer == "1":
    buy_shape()
if answer == "2":
    buy_nitro()
if answer == "3":
    buy_dust()
if answer == "4":
    buy_cinnabar()

