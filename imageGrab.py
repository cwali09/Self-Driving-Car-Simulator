import numpy as np
from PIL import ImageGrab
import cv2
import time


def process_img(image):
    original_image = image
    # Conversion to grey scale
    greyed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Edge detection in greyed image
    greyed_img = cv2.Canny(greyed_img, threshold1 = 200, threshold2 = 300)
    return greyed_img


def main(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        screen =  np.array(ImageGrab.grab(bbox=(0,40,600,640))) # X1,Y1,X2,Y2
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
#main()
from IPYthon.display import Image
Image(filename='edge-detection.png')