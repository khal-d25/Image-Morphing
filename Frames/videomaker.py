import cv2
import numpy as np
import glob

img_array = []
K=1
N=20


img0 = cv2.imread('morphedframe0.jpg')
height, width, layers = img0.shape
size = (width, height)
img_array.append(img0)

for K in range(N+1):
    img = cv2.imread('morphedframe%d.jpg'%K)
    img_array.append(img)





out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'),15,size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

                
