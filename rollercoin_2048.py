import numpy as np
import pyautogui
import os
import matplotlib.pyplot as plt
import cv2
import time
from time import sleep
import random
from PIL import Image

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

def play_2048(sx, sy):
    timeout = time.time() + 75 #+ random.randint(5,600)
    while time.time() < timeout:
            
        draw = np.random.choice(["up","right","down","left"], 1, p=[0.05, 0.1, 0.45, 0.4])
        pyautogui.press(draw)
        sleep(0.2)

    print("Timeout hit, sleeping for 6 more")
    sleep_plus(6)
    
    return True

    

    