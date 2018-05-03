#### Handwritten Digit classification using the entire MNIST Dataset from http://yann.lecun.com/exdb/mnist/  
* The training and the test set consist of 60,000 and 10,000 samples respectively. Each sample is a 28x28 pixel image.  

* The data in the files were parsed using [**python-mnist**](https://github.com/sorki/python-mnist)  
* There was no preprocessing attempted on the data   
* The classification was implemented using a 3 layer neural network with 784 input units, 300 hidden units and 10 output units.  
* Due to the enormous processing requirements, this notebook had to be implemented in [Google Colaboratory](https://colab.research.google.com).  
* Classification accuracy obtained on the test set: **94.58 %**
* Even with 300 units in the hidden layer the network is still suffering from bias
