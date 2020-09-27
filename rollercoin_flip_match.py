import numpy as np
import pyautogui
import os
import matplotlib.pyplot as plt
import cv2
import time
# img = pyautogui.screenshot()
# img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
# #get info from img
# height, width, channels = img.shape
# #Returns the mouse co-ordinates of the block
# #in the given index position

def position_matrix(xplus=250, yplus=250):
    start_x , start_y = 650, 150
    matrix = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append([{
                "left": start_x + i*xplus, 
                "right": start_x + (i+1)*xplus,

                "top": start_y + j*yplus,
                "bottom": start_y + (j+1)*yplus,
            }])
        matrix.append(row)

    return np.array(matrix).reshape((4,4))

matrix = position_matrix()
print(matrix)
print(np.array(matrix).shape)

time.sleep(5)
            
patterns = np.zeros(shape=(3,4))
#rows
for i in range(4):
    #columns
    for j in range(4):
        #screen positions
        x = matrix[i][j]["left"]
        y = matrix[i][j]["top"]

        #Click on this block
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click(x=x, y=y, clicks=1, button='left')
        print("Clicked on Position: ", x, y)

        #Take screenshot
        time.sleep(0.5)
        img = pyautogui.screenshot()

        #Await turnover / match animation
        time.sleep(2)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        block = img[x:x+250, y:y+250]
        cv2.imwrite(f"coin_imgs/{i}{j}.bmp", block)
        #Extract pattern from this block
        

        #Store pattern
        # patterns[i,j] = pat

        #Check if pattern is already in storage
        # match = [(i,j) if pat == patterns[i,j] else (-1,-1) for i in range(3) for j in range(4)]
