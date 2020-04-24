def sdpoints(e1x,e1y,e2x,e2y,x0,y0,m):
    alpha=m[0][0]
    beta =m[1][0]
    a=x0+(alpha*e1x)+(beta*e2x)
    b=y0+(alpha*e1y)+(beta*e2y)
    a=round(a)
    b=round(b)
    a=int(a)
    b=int(b)
    return a,b
    
