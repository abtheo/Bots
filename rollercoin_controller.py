import numpy as np
import pyautogui
import os
import cv2
from time import sleep
from PIL import Image
import random
import time
import mss

# def resolution_conv():
#     1372 * x = 1920
#     700 * y = 1080


redeem_btn = Image.open(r"coin_imgs/blu.png")
def redeem_and_return():
    # sleep(45)
    img = np.array(pyautogui.screenshot())
    try:
        x, y = find_matches(img, redeem_btn)[0]
    #Verification failed, force reload
    except:
        print("Failed to redeem, hard refreshing")
        pyautogui.press('f6') #urlbar
        sleep(0.1)
        pyautogui.typewrite("https://rollercoin.com/game/choose_game")
        sleep(0.1)
        pyautogui.press('enter')
        sleep_plus(90)
        return False

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

def play_blaster():
    timeout = time.time() + 40
    # pyautogui.keyDown("space")
    count = 0
    while time.time() < timeout:
        #Shoot up always
        pyautogui.keyDown("space")
        pyautogui.keyDown("up")

        #Move to sides 
        t = count % 50
        if t > 10 and t <= 15:
            pyautogui.keyUp("left")
            pyautogui.keyDown("right")
        elif t > 25 and t <= 30:
            pyautogui.keyUp("right")
            pyautogui.keyDown("left")
        elif t > 40 and t <= 50:
            coin = np.random.rand()
            if coin >= 0.5:
                pyautogui.keyUp("right")
                pyautogui.keyDown("left")
            else:
                pyautogui.keyUp("left")
                pyautogui.keyDown("right")
            


        count += 1

        # sleep(0.1)
        # leftright = 1
        # for i in range(100):
        #     sleep(0.05)
        #     pyautogui.press("up")
        #     sleep(0.05)
        #     if leftright % 2 == 0:
        #         sleep(0.05)
        #         pyautogui.press("left")
        #     else:
        #         sleep(0.05)
        #         pyautogui.press("right")
            
        # pyautogui.keyUp("right")
        # pyautogui.keyUp("left")
        # leftright += 1

    #free the keys
    pyautogui.keyUp("up")
    pyautogui.keyUp("space")
    return True

def play_2048():
    timeout = time.time() + 60 #+ random.randint(5,600)
    while time.time() < timeout:
            
        draw = np.random.choice(["up","right","down","left"], 1, p=[0.05, 0.1, 0.45, 0.4])
        pyautogui.press(draw)
        # sleep(0.2)

    return True

def play_coinmatch():    
    timeout = time.time() + 60

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
    
    return True

def play_coin_flip_advanced():
    tile_img = Image.open(r"coin_imgs/coinflip_back.png")

    #Locate coins in grid
    img = pyautogui.screenshot()
    sleep(0.5)
    #Lose focus to freeze timer
    pyautogui.press("win")

    grid = find_matches(img, tile_img)
    print(f"Found {len(grid)} matches")

    #Filter out close duplicates from grid
    prev_x, prev_y = grid[0][0], grid[0][1]
    thin_grid = [grid[0]]
    for x,y in grid[1:]:
        if (y > prev_y + 2) or (y < prev_y):
            thin_grid.append((x,y))

        prev_x, prev_y = x, y

    grid = thin_grid
    print(f"Reduced to {len(grid)} matches")

    #Resume
    pyautogui.click(150, 150)

    with mss.mss() as sct:
        coins = []
        for tile in grid:
            #Flip tile
            pyautogui.click(*tile)
            sleep(0.5)
            #Get coloured pixel
            bbox = (tile[0], tile[1], tile[0] + 8, tile[1] + 8)
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

def select_game(sx, sy, fx, fy):
    pyautogui.click(sx, sy)
    pyautogui.click(sx, sy)
    sleep_plus(2)
    pyautogui.click(fx, fy)#Play fullscreen
    pyautogui.click(fx, fy)#Play fullscreen MATCH
    sleep(3)
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
# flags  = Image.open(r"coin_imgs/flag_1920.png")
# coords = find_matches(home, flags)
# #Zip gameID to button positions
# games = ["coinclick", "cryptonoid", "2048", "surfer", "blaster", "coinmatch", "coinflip", "rocket", "hamster", "drham"]
# buttons = dict(zip(games, coords))
# print(buttons)

#lazy lol
# buttons = {'coinclick': (384, 458), 'cryptonoid': (384, 651), '2048': (384, 843), 'surfer': (384, 1036), 'blaster': (827, 458), 'coinmatch': (827, 651), 'coinflip': (827, 843), 'rocket': (1270, 458), 'hamster': (1270, 651), 'drham': (1270, 843)}
buttons = {'coinclick': (511, 367), 'cryptonoid': (511, 521), '2048': (511, 675), 'surfer': (511, 829), 'blaster': (865, 367), 'coinmatch': (865, 521), 'coinflip': (865, 675), 'rocket': (1220, 367), 'hamster': (1220, 521), 'drham': (1220, 675)}
#MAIN LOOP
while True:
    sleep_plus(1)
    #Coinflip
    print("Playing CoinFlip")
    select_game(buttons["coinflip"][0], buttons["coinflip"][1],930,460)
    play_coin_flip_advanced()
    redeem_and_return()
    sleep_plus(45)

    #Blaster!
    # print("Playing Blaster!")
    # select_game(buttons["blaster"][0], buttons["blaster"][1],930,600)
    # play_blaster()
    # redeem_and_return()
    # sleep_plus(45)
    #Coinmatch
    # print("Playing Coinmatch!")
    # select_game(buttons["coinmatch"][0], buttons["coinmatch"][1], 930,562)
    # play_coinmatch()
    # redeem_and_return()
    # sleep_plus(45)
    #2048
    # print("Playing 2048!")
    # select_game(buttons["2048"][0], buttons["2048"][1],930,600)
    # play_2048()
    # redeem_and_return()
    # sleep_plus(90)

