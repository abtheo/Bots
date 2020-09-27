import numpy as np
import pyautogui
import os
import matplotlib.pyplot as plt
import cv2
import time
from time import sleep
import random
from PIL import Image

redeem_btn   = Image.open(r"coin_imgs/blu.png")

def find_matches(haystack, needle):
    arr_h = np.asarray(haystack)
    arr_n = np.asarray(needle)

    y_h, x_h = arr_h.shape[:2]
    y_n, x_n = arr_n.shape[:2]

    xstop = x_h - x_n + 1
    ystop = y_h - y_n + 1

    matches = []
    for xmin in range(0, xstop):
        for ymin in range(0, ystop):
            xmax = xmin + x_n
            ymax = ymin + y_n

            arr_s = arr_h[ymin:ymax, xmin:xmax]     # Extract subimage
            arr_t = (arr_s == arr_n)                # Create test matrix
            if arr_t.all():                         # Only consider exact matches
                matches.append((xmin,ymin))

    return matches

def sleep_plus(n):
    sleep(n + random.randint(0,5) + np.random.rand())

sleep(5)
pyautogui.click(450, 860)#Main screen
sleep(5)
pyautogui.click(930,600)#Play fullscreen

timeout = time.time() + 75 #+ random.randint(5,600)
count = 0
while True:
    if time.time() > timeout:
        # pyautogui.press('f5')
        print("Timeout hit, sleeping for 6 more")
        sleep_plus(6)
        img = np.array(pyautogui.screenshot())

        coords = find_matches(img, redeem_btn)
        coords = coords[:min(len(coords),5)]
        for x, y in coords:
            print("Clicking redeem @ ", x, y)
            pyautogui.click(x,y)
            sleep_plus(0.5)

        # pyautogui.click(1144,617)
        # pyautogui.click(940,590)
        # sleep_plus(0.5)
        # pyautogui.click(954,750)

        # hold = time.time()
        # while time.time() > hold+75:
        #     draw = np.random.choice(["up","right","down","left"], 1, p=[0.05, 0.1, 0.45, 0.4])
        #     pyautogui.press(draw)
        #     sleep(0.2)

        print("Awaiting 95 for redeem")
        sleep_plus(95)
        print("Click Play Again to return to main screen. Sleeping for 180")
        pyautogui.scroll(999, x=0,y=0)
        sleep(1.5)
        pyautogui.click(1138, 686) # Play again
        sleep_plus(270)
        print("Reset timer for 90, clicking replay")
        timeout = time.time() + 90
        pyautogui.click(450, 860)#Main screen
        print("Play again!")
        sleep(5)
        pyautogui.click(930,600)#Play fullscreen

        

    draw = np.random.choice(["up","right","down","left"], 1, p=[0.05, 0.1, 0.45, 0.4])
    pyautogui.press(draw)
    sleep(0.2)

    # count +=1

    # if count > 99999:
    #     print("HARD RESET")
    #     sleep(5)
    #     pyautogui.press('f5')
    #     sleep(180)
    #     count = 0
    #     pyautogui.click(450, 860)#Main screen
    #     sleep(5)
    #     pyautogui.click(930,600)#Play fullscreen
    #     timeout = time.time() + 75

    

    