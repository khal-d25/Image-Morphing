import numpy as np


def alphabeta(e1x, e2x, e1y, e2y, x0, y0, x, y):
    C= np.array([[x-x0],[y-y0]])
    B = np.array([[e1x,e2x],[e1y,e2y]])
    B = np.linalg.inv(B)
    A = np.dot(B,C)
    return A
    
