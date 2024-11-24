x = ['a','b']
y = ['c','d']

def complex_mult(x,y):
    e = x[0]*y[0]-x[1]*y[1]
    f = x[0]*y[1]+x[1]*y[0]
    print(e,f)

complex_mult([0,1], [2,3])