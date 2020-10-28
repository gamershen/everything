import pyautogui
width,height = pyautogui.size()

position = pyautogui.position()

pyautogui.dragTo(position[0]+250,position[1])#top right
pyautogui.dragTo(position[0]+250,position[1]+250)#bot right
pyautogui.dragTo(position[0],position[1]+250)#bot left
pyautogui.dragTo(position[0],position[1])#top left

pyautogui.moveTo(position[0]+125,position[1]-125)#top left
pyautogui.dragTo(position[0]+375,position[1]-125)#top right
pyautogui.dragTo(position[0]+375,position[1]+125)#bot right
pyautogui.dragTo(position[0]+125,position[1]+125)#bot left
pyautogui.dragTo(position[0]+125,position[1]-125)#top left

pyautogui.dragTo(position[0],position[1])
pyautogui.moveTo(position[0]+375,position[1]-125)
pyautogui.dragTo(position[0]+250,position[1])
pyautogui.moveTo(position[0]+375,position[1]+125)
pyautogui.dragTo(position[0]+250,position[1]+250)
pyautogui.moveTo(position[0]+125,position[1]+125)
pyautogui.dragTo(position[0],position[1]+250)
