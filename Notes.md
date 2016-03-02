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
* 


We define a memprocessor as an object defined by the four-tuple $(x,y,z,\sigma)$ where x is the state of the memprocessor, y is the array of internal variables,z the array of variables that connect from one memprocessor to other memprocessors, and  an operator that defines the evolution

$\sigma[x,y,z] = x', y' \\$

In neural networks we have a few different types of memprocessor
* Feedforward $\sigma[x, w \,and\, b] = y $ although these do not seem to be an interesting version of memprocess. The only fit in the trivial case of ... 
* Recurrent $\sigma[x,w \,and\, b, y^{t-1}] = y^t $... 
  * y = x for vanilla? 
  * LTSM... x = h(t), y = c(t), z = [h(t)], \sigma = ?!?
  * 
  
they define a memprocessor as 
$
x_{ex}(t) = g(x_{in},u(t),t)u(t) \\
x_{in}(t) =f(x_{in},u(t),t) \\
$
less cryptically
$
V = IR \\
R(t) = g(R(t),I(t),t) \\
V = g(R(t),I(t),t) I(t) \\
\frac{\partial R}{\partial t} = f(R(t),I(t),t)  \\
$
and in our language
$
y = w \cdot x \\
w(t) = g(w(t),x(t),t) \\
y(t) = g(w(t),x(t),t) x(t) \\
\frac{\partial w}{\partial t} = f(w(t),x(t),t)  \\
$

where g() would be the activation function? no. not for time

cool, this seem right.??

according to them the time evolution of the system
$$w(t+T) - w(t) = \int_{t}^{t+T} f(w(\tau),x(w(\tau),y(\tau)),\tau) \parital \tau$$
