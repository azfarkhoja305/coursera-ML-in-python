
import matplotlib.pyplot as plt

def plotScatter(X,y):
    """Plotting a scatter plot of the data"""
    plt.figure(figsize=(9,6),dpi=80)
    plt.scatter(X,y,c='r',marker='x',label = "Training Data")
    plt.legend(loc = 'upper left')
    plt.xlabel('Population of a City in 10,000s')
    plt.ylabel('Profit in $10,000s')
    plt.ylim(ymin=-5)
    
