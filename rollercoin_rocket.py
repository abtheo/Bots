import numpy as np
import pyautogui
import os
import cv2
from time import sleep


def play_rocket():
    while True:
        pyautogui.click()
        sleep(np.random.rand())
    