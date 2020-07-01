def lax_wendroff(a, b, h, k, T, alph, f):
    
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
    for i in np.arange(a, b+h, h):
        U.append(f(i))
        U1.append(0)
    
    returnList.append(U)
    
    for time in np.arange(0, T):
        
        for j in range(1, len(U)-1):
            U1[j] = U[j]-(((alph*lambd)/2)*(U[j+1]-U[j-1]))+((((alph*lambd)**2)/2)*(U[j+1] - (2*U[j]) + U[j-1]))
            
        U1[-1] = U1[-2]
        timeList.append(time*k)
        returnList.append(U1)
        U=U1
    
    return returnList
