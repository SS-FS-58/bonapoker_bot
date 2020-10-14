import cv2
from matplotlib import pyplot as plt
import numpy as np
import keyboard 

if __name__ == '__main__':
    
    filename = r"e:\1_Previous_Projects\24_Poker_bot\bonapoker_bot\screenshot_log\test3.png"
        
    plt.imshow(cv2.imread(filename))
    plt.show()
    # Using Keyboard module in Python 

    
    # # It writes the content to output 
    # keyboard.write("124\n") 
    # # It writes the keys r, k and endofline  
    # keyboard.press_and_release('shift + r, shift + k, \n') 
    # keyboard.press_and_release('R, K') 
    
    # # it blocks until ctrl is pressed 
    # keyboard.wait('Ctrl')
    # print("ok")