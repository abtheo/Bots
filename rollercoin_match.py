import numpy as np
import pyautogui
import os
import cv2
from time import sleep




while True:
    pyautogui.click()
    sleep(0.6)
    
def play_coinmatch(sx, sy):    

    timeout = time.time() + 75
    while time.time() < timeout:
        #Row grid spaces
        for x in range(535, 1495, 120):
            for y in range(110, 1070, 120):
                #Move mouse to block
                pyautogui.moveTo(x, y, duration=1)
                sleep(1)
                #Pick action and drag block
                action = np.random.choice(["up","right","down","left"], 1)
                pyautogui.click()
                if action == "up":
                    pyautogui.dragRel(xOffset=0,yOffset=-120)
                elif action == "right"
                    pyautogui.dragRel(xOffset=120,yOffset=0)
                elif action == "down"
                    pyautogui.dragRel(xOffset=0,yOffset=120)
                elif action == "left"
                    pyautogui.dragRel(xOffset=-120,yOffset=0)


    print("Timeout hit, sleeping for 6 more")
    sleep_plus(6)
    
    return True




