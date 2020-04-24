import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
from pts import myPts
from intriangle import intriangle
from alphabeta import alphabeta
from sdpoints import sdpoints

cv2.destroyAllWindows()

src =[]
des=[]
p = []

color = (0,0,255)
thickness = 3

#read images
srcimg = cv2.imread('ak1.jpg')                          #source image
desimg = cv2.imread('tw1.jpg')                          #destinaniton image

srcimg1 = cv2.resize(srcimg,(500,500))
desimg1 = cv2.resize(desimg,(500,500))
srcimg2 = cv2.resize(srcimg,(500,500))
desimg2 = cv2.resize(desimg,(500,500))


#press a after selecting the three points to form triangle
u, v = myPts(srcimg1)
u, v = myPts(desimg1)

a= u[0]*u[0] + v[0]*v[0]
b= u[1]*u[1] + v[1]*v[1]
c= u[2]*u[2] + v[2]*v[2]
while(1):
        if((a<=b) and (a<=c)):
                src.append(u[0])
                src.append(v[0])
                des.append(u[3])
                des.append(v[3])
        
        elif((b<=a) and (b<=c)):
                src.append(u[1])
                src.append(v[1])
                des.append(u[4])
                des.append(v[4])
        
        elif((c<=b) and (c<=a)):
                src.append(u[2])
                src.append(v[2])
                des.append(u[5])
                des.append(v[5])
        break

d= u[0]*u[0] + ((500-v[0])*(500-v[0]))
e= u[1]*u[1] + ((500-v[1])*(500-v[1]))
f= u[2]*u[2] + ((500-v[2])*(500-v[2]))
while(1):
        if((d<=e) and (d<=f)):
                src.append(u[0])
                src.append(v[0])
                des.append(u[3])
                des.append(v[3])
                if(src[0]==u[1]):
                        src.append(u[2])
                        src.append(v[2])
                        des.append(u[5])
                        des.append(v[5])
                else:
                        src.append(u[1])
                        src.append(v[1])
                        des.append(u[4])
                        des.append(v[4]) 

        elif((e<=d) and (e<=f)):
                src.append(u[1])
                src.append(v[1])
                des.append(u[4])
                des.append(v[4])
                if(src[0]==u[0]):
                        src.append(u[2])
                        src.append(v[2])
                        des.append(u[5])
                        des.append(v[5])
                else:
                        src.append(u[0])
                        src.append(v[0])
                        des.append(u[3])
                        des.append(v[3])

        elif((f<=e) and (f<=d)):
                src.append(u[2])
                src.append(v[2])
                des.append(u[5])
                des.append(v[5])
                if(src[0]==u[0]):
                        src.append(u[1])
                        src.append(v[1])
                        des.append(u[4])
                        des.append(v[4])
                else:
                        src.append(u[0])
                        src.append(v[0])
                        des.append(u[3])
                        des.append(v[3])
        break
                
print(src)
print(des)

#forming triangles
cv2.line(srcimg2,(src[0],src[1]) , (0,0), color, thickness)
cv2.line(srcimg2,(src[0],src[1]) , (0,499), color, thickness)
cv2.line(srcimg2,(src[0],src[1]) , (499,0), color, thickness)
cv2.line(srcimg2,(src[0],src[1]) , (src[2],src[3]), color, thickness)
cv2.line(srcimg2,(src[0],src[1]) , (src[4],src[5]), color, thickness)
cv2.line(srcimg2,(src[2],src[3]) , (0,499), color, thickness)
cv2.line(srcimg2,(src[2],src[3]) , (499,499), color, thickness)
cv2.line(srcimg2,(src[2],src[3]) , (src[4],src[5]), color, thickness)
cv2.line(srcimg2,(src[4],src[5]) , (499,0), color, thickness)
cv2.line(srcimg2,(src[4],src[5]) , (499,499), color, thickness)
cv2.imwrite(("Lines Source.jpg"),srcimg2)

cv2.line(desimg2,(des[0],des[1]) , (0,0), color, thickness)
cv2.line(desimg2,(des[0],des[1]) , (0,499), color, thickness)
cv2.line(desimg2,(des[0],des[1]) , (499,0), color, thickness)
cv2.line(desimg2,(des[0],des[1]) , (des[2],des[3]), color, thickness)
cv2.line(desimg2,(des[0],des[1]) , (des[4],des[5]), color, thickness)
cv2.line(desimg2,(des[2],des[3]) , (0,499), color, thickness)
cv2.line(desimg2,(des[2],des[3]) , (499,499), color, thickness)
cv2.line(desimg2,(des[2],des[3]) , (des[4],des[5]), color, thickness)
cv2.line(desimg2,(des[4],des[5]) , (499,0), color, thickness)
cv2.line(desimg2,(des[4],des[5]) , (499,499), color, thickness)
cv2.imwrite(("Lines Destination.jpg"),desimg2)


while(1):
        cv2.imshow("Source Lines",srcimg2)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('a'):
                cv2.destroyAllWindows()
                break


while(1):
        cv2.imshow("Destination Lines",desimg2)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('a'):
                cv2.destroyAllWindows()
                break

#creating new image with zero pixel values
temp = np.zeros(shape=[500,500,3],dtype=np.uint8)
#cv2.imshow("blank",temp)
N=20
K=0
f=499
i= 0
j= 0

for K in range(N+1):
        q1=((N-K)/N)*src[0]+(K/N)*des[0]
        p.append(q1)
        w1=((N-K)/N)*src[1]+(K/N)*des[1]
        p.append(w1)
        q2=((N-K)/N)*src[2]+(K/N)*des[2]
        p.append(q2)
        w2=((N-K)/N)*src[3]+(K/N)*des[3]
        p.append(w2)
        q3=((N-K)/N)*src[4]+(K/N)*des[4]
        p.append(q3)
        w3=((N-K)/N)*src[5]+(K/N)*des[5]
        p.append(w3) 
#loop for every pixel
        for i in range(f+1):
                for j in range(f+1):
                        if intriangle(p[0],p[1],0,0,0,499,i,j)==1:        
                                e1x=0-p[0]
                                e1y=0-p[1]
                                e2x=0-p[0]                                      
                                e2y=499-p[1]
                                A = alphabeta(e1x,e2x,e1y,e2y,p[0],p[1],i,j)      
                                sx,sy =sdpoints(0-src[0],0-src[1],0-src[0],499-src[1],src[0],src[1],A) 
                                dx,dy =sdpoints(0-des[0],0-des[1],0-des[0],499-des[1],des[0],des[1],A)
                                red=((N-K)/N)*(srcimg1[sx,sy,0])+(K/N)*(desimg1[dx,dy,0])
                                green=((N-K)/N)*(srcimg1[sx,sy,1])+(K/N)*(desimg1[dx,dy,1])
                                blue=((N-K)/N)*(srcimg1[sx,sy,2])+(K/N)*(desimg1[dx,dy,2])
                                 
                                temp[i,j,0]=red
                                temp[i,j,1]=green
                                temp[i,j,2]=blue
           
                        elif intriangle(p[0],p[1],p[2],p[3],0,499,i,j)== 1:
                                e1x=0-p[0]
                                e1y=499-p[1]
                                e2x=p[2]-p[0]
                                e2y=p[3]-p[1]
      
                                A=alphabeta(e1x,e2x,e1y,e2y,p[0],p[1],i,j)
                                sx,sy =sdpoints(0-src[0],499-src[1],src[2]-src[0],src[3]-src[1],src[0],src[1],A)
                                dx,dy =sdpoints(0-des[0],499-des[1],des[2]-des[0],des[3]-des[1],des[0],des[1],A)
                                red=((N-K)/N)*(srcimg1[sx,sy,0])+(K/N)*(desimg1[dx,dy,0])
                                green=((N-K)/N)*(srcimg1[sx,sy,1])+(K/N)*(desimg1[dx,dy,1])
                                blue=((N-K)/N)*(srcimg1[sx,sy,2])+(K/N)*(desimg1[dx,dy,2])
                 
                                temp[i,j,0]=red
                                temp[i,j,1]=green
                                temp[i,j,2]=blue

                        elif intriangle(0,499,p[2],p[3],499,499,i,j)==1:
                                e1x=0-p[2]
                                e1y=499-p[3]
                                e2x=499-p[2]
                                e2y=499-p[3]
        
                                A=alphabeta( e1x,e2x,e1y,e2y,p[2],p[3],i,j)
                                sx,sy=sdpoints(0-src[2],499-src[3],499-src[2],499-src[3],src[2],src[3],A)
                                dx,dy=sdpoints(0-des[2],499-des[3],499-des[2],499-des[3],des[2],des[3],A)
                                a1=srcimg1[sx,sy,0]
                                z1=desimg1[dx,dy,0]
                                red=((N-K)/N)*(a1)+(K/N)*(z1)
                                #red=((N-K)/N)*(srcimg1[sx,sy,0])+(K/N)*(desimg1[dx,dy,0])
                                green=((N-K)/N)*(srcimg1[sx,sy,1])+(K/N)*(desimg1[dx,dy,1])
                                blue=((N-K)/N)*(srcimg1[sx,sy,2])+(K/N)*(desimg1[dx,dy,2])
                 
                                temp[i,j,0]=red
                                temp[i,j,1]=green
                                temp[i,j,2]=blue

                        elif intriangle(p[4],p[5],p[2],p[3],499,499,i,j)==1:
                                e1x=p[4]-p[2]
                                e1y=p[5]-p[3]
                                e2x=499-p[2]
                                e2y=499-p[3]
    
        
                                A=alphabeta(e1x,e2x,e1y,e2y,p[2],p[3],i,j)
                                sx,sy=sdpoints(src[4]-src[2],src[5]-src[3],499-src[2],499-src[3],src[2],src[3],A)
                                dx,dy=sdpoints(des[4]-des[2],des[5]-des[3],499-des[2],499-des[3],des[2],des[3],A)
                                red=((N-K)/N)*(srcimg1[sx,sy,0])+(K/N)*(desimg1[dx,dy,0])
                                green=((N-K)/N)*(srcimg1[sx,sy,1])+(K/N)*(desimg1[dx,dy,1])
                                blue=((N-K)/N)*(srcimg1[sx,sy,2])+(K/N)*(desimg1[dx,dy,2])
                 
                                temp[i,j,0]=red
                                temp[i,j,1]=green
                                temp[i,j,2]=blue

                        elif intriangle(p[4],p[5],499,0,499,499,i,j)==1:
                                e1x=499-p[4]
                                e1y=0-p[5]
                                e2x=499-p[4]
                                e2y=499-p[5]
        
                                A=alphabeta( e1x,e2x,e1y,e2y,p[4],p[5],i,j)
                                sx,sy=sdpoints(499-src[4],0-src[5],499-src[4],499-src[5],src[4],src[5],A)
                                dx,dy=sdpoints(499-des[4],0-des[5],499-des[4],499-des[5],des[4],des[5],A)
                                red=((N-K)/N)*(srcimg1[sx,sy,0])+(K/N)*(desimg1[dx,dy,0])
                                green=((N-K)/N)*(srcimg1[sx,sy,1])+(K/N)*(desimg1[dx,dy,1])
                                blue=((N-K)/N)*(srcimg1[sx,sy,2])+(K/N)*(desimg1[dx,dy,2])
                 
                                temp[i,j,0]=red
                                temp[i,j,1]=green
                                temp[i,j,2]=blue

                        elif intriangle(p[0],p[1],p[4],p[5],499,0,i,j)==1:
                                e1x=p[0]-p[4]
                                e1y=p[1]-p[5]
                                e2x=499-p[4]
                                e2y=0-p[5]
      
                                A=alphabeta( e1x,e2x,e1y,e2y,p[4],p[5],i,j)
                                sx,sy=sdpoints(src[0]-src[4],src[1]-src[5],499-src[4],0-src[5],src[4],src[5],A)
                                dx,dy=sdpoints(des[0]-des[4],des[1]-des[5],499-des[4],0-des[5],des[4],des[5],A)
                                red=((N-K)/N)*(srcimg1[sx,sy,0])+(K/N)*(desimg1[dx,dy,0])
                                green=((N-K)/N)*(srcimg1[sx,sy,1])+(K/N)*(desimg1[dx,dy,1])
                                blue=((N-K)/N)*(srcimg1[sx,sy,2])+(K/N)*(desimg1[dx,dy,2])
                 
                                temp[i,j,0]=red
                                temp[i,j,1]=green
                                temp[i,j,2]=blue

                        elif intriangle(p[0],p[1],0,0,499,0,i,j)==1:
                                e1x=0-p[0]
                                e1y=0-p[1]
                                e2x=499-p[0]
                                e2y=0-p[1]
                     
                                A=alphabeta( e1x,e2x,e1y,e2y,p[0],p[1],i,j)
                                sx,sy=sdpoints(0-src[0],0-src[1],499-src[0],0-src[1],src[0],src[1],A)
                                dx,dy=sdpoints(0-des[0],0-des[1],499-des[0],0-des[1],des[0],des[1],A)
                                red=((N-K)/N)*(srcimg1[sx,sy,0])+(K/N)*(desimg1[dx,dy,0])
                                green=((N-K)/N)*(srcimg1[sx,sy,1])+(K/N)*(desimg1[dx,dy,1])
                                blue=((N-K)/N)*(srcimg1[sx,sy,2])+(K/N)*(desimg1[dx,dy,2])
                 
                                temp[i,j,0]=red
                                temp[i,j,1]=green
                                temp[i,j,2]=blue

                        elif intriangle(p[0],p[1],p[2],p[3],p[4],p[5],i,j)==1:
                                e1x=p[0]-p[2]
                                e1y=p[1]-p[3]
                                e2x=p[4]-p[2]
                                e2y=p[5]-p[3]
       
                                A=alphabeta( e1x,e2x,e1y,e2y,p[2],p[3],i,j)
                                sx,sy=sdpoints(src[0]-src[2],src[1]-src[3],src[4]-src[2],src[5]-src[3],src[2],src[3],A)
                                dx,dy=sdpoints(des[0]-des[2],des[1]-des[3],des[4]-des[2],des[5]-des[3],des[2],des[3],A)
                                red=((N-K)/N)*(srcimg1[sx,sy,0])+(K/N)*(desimg1[dx,dy,0])
                                green=((N-K)/N)*(srcimg1[sx,sy,1])+(K/N)*(desimg1[dx,dy,1])
                                blue=((N-K)/N)*(srcimg1[sx,sy,2])+(K/N)*(desimg1[dx,dy,2])
                 
                                temp[i,j,0]=red
                                temp[i,j,1]=green
                                temp[i,j,2]=blue
        
#display final image
        while(1):
                cv2.imshow("Temp Lines",temp)
                
                k = cv2.waitKey(0) & 0xFF
                if k == ord('a'):
                        #filename = '"%d"morphed frame' 
                        cv2.imwrite(("morphedframe%d.jpg"%K),temp)
                        cv2.destroyAllWindows()
                        break       
    
                


        







