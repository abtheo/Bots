import numpy as np
import pyautogui
import os
import cv2
from time import sleep
from PIL import Image
import random
import time

#from rollercoin_2048 import play_2048

def dragTo(from_x, from_y, to_x, to_y):
    try:
        pyautogui.mouseDown(from_x, from_y)
    except PermissionError:
        pass

    try:
        pyautogui.mouseUp(to_x, to_y)
    except PermissionError:
        pass

redeem_btn = Image.open(r"coin_imgs/blu.png")
def redeem_and_return():
    img = np.array(pyautogui.screenshot())

    x, y = find_matches(img, redeem_btn)[0]

    print("Clicking redeem @ ", x, y)
    pyautogui.click(x,y)
    sleep_plus(0.5)
    print("Awaiting 35 for redeem")
    sleep_plus(35)
    print("Click Play Again to return to main screen.")
    pyautogui.scroll(999, x=0,y=0)
    sleep(1.5)
    pyautogui.click(1138, 686) # Play again
    return True

def play_rocket():
    for i in range(3):
        pyautogui.click(1120, 250)#Out of the way

    timeout = time.time() + 40
    while time.time() < timeout:
        pyautogui.click()
        sleep(np.random.uniform(0.3,0.44))

    print("Timeout hit, sleeping for 6 more")
    sleep_plus(6)
    return True

def play_2048():
    timeout = time.time() + 60 #+ random.randint(5,600)
    while time.time() < timeout:
            
        draw = np.random.choice(["up","right","down","left"], 1, p=[0.05, 0.1, 0.45, 0.4])
        pyautogui.press(draw)
        sleep(0.2)

    print("Timeout hit, sleeping for 6 more")
    sleep_plus(6)
    
    return True

def play_coinmatch():    
    timeout = time.time() + 65

    upright = 1
    while time.time() < timeout:
        #Row grid spaces
        for x in range(535, (1495-120), 120):
            for y in range((110+120), (1070-120), 120):
                #Pick action and click block
                # action = np.random.choice(["up","right","down","left"], 1)


                #Avoid middle
                if (x > 500 and x < 1455) and (y > 650 and y < 900):
                    continue


                pyautogui.click(x, y)
                sleep(0.1)
                if upright % 2 == 0:
                    pyautogui.click(x+120, y)
                else:
                    pyautogui.click(x, y-120)
                
                upright += 1
        # img = np.array(pyautogui.screenshot())
        # matches = find_matches(img, redeem_btn)
        # if len(matches) > 0:
        #     print("Found redeem button @", matches)
        #     return True


    print("Timeout hit, sleeping for 6 more")
    sleep_plus(6)
    
    return True


def select_game(sx, sy, fx, fy):
    print("Playing Game!")
    pyautogui.click(sx, sy)
    pyautogui.click(sx, sy)
    sleep_plus(2)
    pyautogui.click(fx, fy)#Play fullscreen
    pyautogui.click(fx, fy)#Play fullscreen MATCH
    sleep(2.5)
    return True

def sleep_plus(n):
    sleep(n + random.randint(0,5) + np.random.rand())

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


print("Starting...")
sleep(5)
#Screenshot to find button positions
home = np.array(pyautogui.screenshot())
print("Screenshot taken!")

#Find flags
flags   = Image.open(r"coin_imgs/flag.png")
coords = find_matches(home, flags)
#Zip gameID to button positions
games = ["coinclick", "cryptonoid", "2048", "surfer", "token", "coinmatch", "flip", "rocket", "hamster", "drham"]
buttons = dict(zip(games, coords))

print(buttons)
#MAIN LOOP
while True:
    sleep_plus(1)
    #Coinmatch
    select_game(buttons["coinmatch"][0], buttons["coinmatch"][1], 930,562)
    play_coinmatch()
    redeem_and_return()
    sleep_plus(1)
    #2048
    select_game(buttons["2048"][0], buttons["2048"][1],930,600)
    play_2048()
    redeem_and_return()
    sleep_plus(1)

