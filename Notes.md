# Honours project



# 311


# 312



# 313


# CS231n

Start with:
* A Conv layer. Test some different window sizes and activation functions?
* Then multi layer Conv. Depth vs breadth
* Pooling and competition
* Normalising - Batch, weight, layer output
* Optimisation - stochastic gradient descent, momentum, ... ??
* Overfitting - Weight decay, dropout
* Initialisation


Add softmax and test between each?


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

Why define a state and internal variables seperately? 
* This shit seems important! Very similar to how quantum computers are supposed to work?
 * Could I implement something like Shors algorithm on one??? That sounds like an interesting project.
* To - do. Simulate the dynamical equations for a 1, 2/3 memprocessor system.
