# Honours project



# 311


# 312



# 313


# CS231n

Start with:
* A Conv layer
   * Test some different window sizes and activation functions?
* Multi layer Conv
   * Depth vs breadth
* Tensors
* Pooling
   * ??
* Normalising
   * Batches, weights, layer outputs
* Optimisation
   * Stochastic gradient descent, momentum, ... ??
* Overfitting
   * Weight decay, dropout
* Initialisation

zero padding?
Add softmax and test between each?

```python
import numpy as np
class Kernel():
    def __init__(self,shape):
        self.weights = np.random.random(shape)

class ConvNet():
    def __init__(self, layershapes):
        self.layershapes = layershapes

        self.init_layers()

    def init_layers(self):
        self.layers = []
        for shape in self.layershapes:
            self.layers.append(Kernel(shape))

    def convolve(self, image, stride = 2):
        #for each layer: #not yet..
        
        n,m = image.shape
        window = self.layershapes[0][-1]
        
        for i in range(n+window):
            for j in range(m):
                pass


if __name__ == '__main__':
    CN = ConvNet([(10,3,5,5)]) #10 kernels, 3 pixels, 5x5 networks
    



"""
WHat is the best way to store the kernels? A nested list?

[
[ Kernel1, Kernel2, Kernel3 ...] #first layer
[ Kernel1, Kernel2, Kernel3 ...] #second layer
[ Kernel1, Kernel2, Kernel3 ...] #third layer
]
"""

```


# Prediction and learning
$
\hat{y} = \sum w x for x \in [0,1], x \in [0,1] \\
error = E = \frac{(y-\hat{y})^2}{2} \\
\frac{\partial E}{\partial \hat{y}} = y - \hat{y} \\
\frac{\partial \hat{y}}{\partial w_i} = x_i  \\
\Delta w = - \alpha \frac{\partial E}{\partial w_i} = - \alpha (y-\hat{y}) x \\
\Psi_{t=0} = 0\\
\Psi_{t} = \sum \Delta w_t \\
\Psi{t = T} =  \\
$

What is $\Psi$?? 

### What is the goal?

* Accuracy = f(errors made) ???    ... idiot
    * No? We want some sort of upper bound on the errors the algorithm will make. (while being accurate??)
    * Yes but, for WMA and halving we know that they are limited by the best expert so 


For backprop, the net can actually get all wrong, as it can choose to listen to the wrong expert. But this doesnt happen as ...
The goal then is to find the lowest upper bound?
# UMM




