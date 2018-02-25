import numpy as np

def cost(X,y,theta):
    m = np.size(y)
    J = (1/(2.0*m))*np.sum(np.power((X.dot(theta)-y),2))
    return J

    
    
    