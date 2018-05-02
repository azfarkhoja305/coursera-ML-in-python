* **ex5data.npz**  
This dataset is divided into three parts  
  * A training set that your model will learn on: X, y
  * A cross validation set for determining the regularization parameter: Xval, yval
  * A test set for evaluating performance. These are “unseen” examples which your model did not see during training: Xtest, ytest

The aim is to implement regularized regression to predict the amount of water flowing out of a dam **(y)** ,
using the change of water level in a reservoir **(X)** .  
The other part deals with some diagnostics of debugging learning algorithms and examining the effects of **Bias vs Variance** . 
