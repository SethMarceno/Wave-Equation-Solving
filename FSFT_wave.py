import numpy as np
import scipy as sp
from scipy import linalg

def FSFT_wave(a, b, h, k, T, f):
    
    '''
    a=starting x boundary
    b=ending x boundary
    h=spacial step
    k=time step
    T=Number of time steps to take
    f=initial function
    '''
    
    lambd = k/h
    M=(b-a)/h
    timeList = []
    returnList = []
    
    U=[]
    U1 = []
    for i in np.arange(a, b, h):
        U.append(f(i))
        U1.append(0)

    for time in np.arange(0, T):
        
        for j in range(0, len(U)-1):
            U1[j] = ((1+lambd)*U[j]) - (lambd*U[j+1])
            
        U1[-1] = U1[-2]
        timeList.append(time*k)
        returnList.append(U1)
        U=U1
    
    return returnList
