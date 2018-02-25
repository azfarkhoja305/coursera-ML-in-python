import numpy as np
import costFunction

def gdescent(X,y,theta,alpha,iters):
    X = np.mat(X); y=np.mat(y); theta = np.mat(theta);
    m = np.size(y)
    J_hist = np.zeros(iters)
    for i in range(0,iters):
        temp = theta - (alpha/m) * (X.T * (X*theta-y))
        theta = temp
        J_hist[i]= costFunction.cost(X,y,theta)
        
    return np.asarray(theta),J_hist

        
        