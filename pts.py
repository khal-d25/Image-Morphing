import numpy as np
import cv2
import matplotlib.pyplot as plt

posListx = []
posListy = []

def myPts(image):
    def onMouse(event, x, y, flags, param):
        global posListx, posListy
       
        if event == cv2.EVENT_LBUTTONDOWN:
            
            posListx.append(x)
            posListy.append(y)
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',onMouse)

    while(1):
        cv2.imshow("image",image)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            return [],[]
            break
        elif k == ord('a'):
            cv2.destroyAllWindows()
            return posListx, posListy
            
            


if __name__ == "__main__":
    srcimg = cv2.imread('dtrump.jpg')                       #source image
    desimg = cv2.imread('tcruz.jpg')                        #destinaniton image


    srcimg1 = cv2.resize(srcimg,(500,500))
    desimg2 = cv2.resize(desimg,(500,500))

    #print(myPts(srcimg1))






    
