import numpy as np
import pyautogui
import os
import cv2
from time import sleep
from PIL import Image
import random
import time
import mss
from scipy.spatial import distance
#from rollercoin_2048 import play_2048


redeem_btn = Image.open(r"coin_imgs/blu.png")
def redeem_and_return():
    sleep(4)
    img = np.array(pyautogui.screenshot())
    try:
        x, y = find_matches(img, redeem_btn)[0]
    except:
        print('Failed to Redeem, hard refresh')
        pyautogui.press('esc')
        sleep(1)
        pyautogui.press('f6')
        sleep(1)
        pyautogui.typewrite('https://rollercoin.com/game/choose_game')
        sleep(1)
        pyautogui.press('enter')
        return False
    
    print("Clicking redeem @ ", x, y)
    pyautogui.click(x,y)
    sleep_plus(0.5)
    print("Awaiting redeem...")
    sleep_plus(25)
    print("Click Play Again to return to main screen.")
    pyautogui.scroll(999, x=0,y=0)
    sleep(1.5)
    pyautogui.click(800, 515) # Play again
    return True

def play_rocket():
    for i in range(3):
        pyautogui.click(185, 250)#Out of the way

    timeout = time.time() + 40
    while time.time() < timeout:
        pyautogui.click()
        sleep(np.random.uniform(0.3,0.44))

    print("Timeout hit, sleeping for 6 more")
    sleep_plus(6)
    return True

tile_img = Image.open(r"coin_imgs/coinflip_back.png")
def play_coin_flip():

    #Locate coins in grid
    sleep(2.5)
    img = np.array(pyautogui.screenshot())
    sleep(0.5)
    #Lose focus to freeze timer
    pyautogui.press(r"'")
    grid = find_matches(img, tile_img)
    #print(f"Found {len(grid)} matches")
    
    #Filter out close duplicates from grid
    try:
        prev_x, prev_y = grid[0][0], grid[0][1]
    except:
        sleep(60)
        return False
    
##    pyautogui.press(r"'")
##    thin_grid = [grid[0]]
##    for x,y in grid[1:]:
##        if ((y > prev_y + 20) or (y < prev_y -20)):
##            thin_grid.append((x,y))
##
##        prev_x, prev_y = x, y
##
##    grid = thin_grid
##    print(f"Reduced to {len(grid)} matches")

    pyautogui.press(r"'")
    #all_distances = [a if distance.euclidean(a, b) > 2 else None for a in grid for b in grid]
    #print(all_distances)
    distances = []
    for i, tile in enumerate(grid):
        distances += [j for j, b in enumerate(grid) \
                       if distance.euclidean(tile, b) < 5.0 and j > i]
        
    distances = np.array(list(set(distances)), dtype=int)
    grid = [grid[i] for i in range(len(grid)) if i not in distances]
    print(f"Reduced to {len(grid)} matches")

    #Resume
    pyautogui.click(10, 10)

    with mss.mss() as sct:
        coins = []
        for tile in grid:
            #Flip tile
            pyautogui.click(*tile)
            sleep(0.5)
            #Get coloured pixel
            bbox = (tile[0], tile[1], tile[0] + 2, tile[1] + 2)
            sct_img = sct.grab(bbox)
            coin_pix = np.array(sct_img.pixels)
            # mss.tools.to_png(sct_img.rgb, sct_img.size, output=f"flip/{tile[0]}_{tile[1]}.png")
            # print("Saved image")
            coins.append(coin_pix)
            sleep(0.5)
            
    #Find all pairs of matches
    for c,coin in enumerate(coins):
        matches = [i for i, match_coin in enumerate(coins) if (match_coin == coin).all() and i >= c]
        if len(matches) < 2: continue

        #Click 'em
        sleep(0.5)
        pyautogui.click(*grid[matches[0]])
        sleep(0.5)
        pyautogui.click(*grid[matches[-1]])
        sleep(0.5)
        
    sleep(1)
    return True

def play_2048():
    timeout = time.time() + 56 #+ random.randint(5,600)
    while time.time() < timeout:
            
        draw = np.random.choice(["up","right","down","left"], 1, p=[0.05, 0.1, 0.45, 0.4])
        pyautogui.press(draw)

    print("Timeout hit, sleeping for 6 more")
    sleep_plus(6)
    
    return True

def play_coinmatch():    
    timeout = time.time() + 65

    upright = 1
    while time.time() < timeout:
        #Row grid spaces
        for x in range(380, (985-85), 85):
            for y in range((80+85), (625-85), 85):
                #Pick action and click block
                # action = np.random.choice(["up","right","down","left"], 1)


                #Avoid middle
                if (x > 300 and x < 950) and (y > 460 and y < 650):
                    continue


                pyautogui.click(x, y)
                sleep(0.1)
                if upright % 2 == 0:
                    pyautogui.click(x+85, y)
                else:
                    pyautogui.click(x, y-85)
                
                upright += 1
        # img = np.array(pyautogui.screenshot())
        # matches = find_matches(img, redeem_btn)
        # if len(matches) > 0:
        #     print("Found redeem button @", matches)
        #     return True

    sleep_plus(6)
    
    return True


def select_game(sx, sy, fx, fy):
    print("Playing Game!")
    pyautogui.click(sx, sy)
    sleep(0.5)
    pyautogui.click(sx, sy)
    sleep(2.5)
    pyautogui.click(fx, fy)#Play fullscreen
    sleep(0.5)
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
##home = np.array(pyautogui.screenshot())
##print("Screenshot taken!")
##
###Find flags
##flags   = Image.open(r"coin_imgs/flag_2.png")
##coords = find_matches(home, flags)
###Zip gameID to button positions
##games = ["coinclick", "cryptonoid", "2048", "token", "coinmatch", "flip", "rocket", "hamster", "drham"]
##buttons = dict(zip(games, coords))

##print(buttons)
buttons = {'coinclick': (235, 340), 'cryptonoid': (235, 494), '2048': (235, 648), 'token': (589, 340), 'coinmatch': (589, 494), 'coinflip': (589, 648), 'rocket': (944, 340), 'hamster': (944, 494), 'drham': (944, 648)}
#MAIN LOOP
while True:
    #Coinflip
    print('Coinflip:')
    select_game(buttons["coinflip"][0], buttons["coinflip"][1], 670, 440)
    play_coin_flip()
    redeem_and_return()
    sleep(180)
    #Coinmatch
##    select_game(buttons["coinmatch"][0], buttons["coinmatch"][1], 670, 400)
##    play_coinmatch()
##    redeem_and_return()
##    sleep(10)
    #2048
    print('2048:')
    select_game(buttons["2048"][0], buttons["2048"][1],670,440)
    play_2048()
    redeem_and_return()
    sleep(180)

