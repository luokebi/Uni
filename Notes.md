# Honours project



# 311

### Equivalence classes
$
x \sim y \\
[x] = [y] \\
[x] \cap [y] \ne \emptyset \\
$

this doesnt quite make sense to me, shouldn't it be a stronger condition? I thought that $[x] \cap [y] \ne \emptyset  =  [x] = [y]$ ???

If $[a] = \{ x \in X \mid a \sim x \} = [x_i]$ ??
If $ [x_{1},x_{55},x_{102}] = \{ x \in X \mid a \sim x \}$ is it possible for $ \{ x \in X \mid b \sim x \} = [x_{55}]$ or must it be the full equivalence class as $a == b$?

# 312

### Sequences
Suppose that a sequence $(x_n)_{n=1}^{\infty} converges to real numbers a and b. Then a = b. Why is this useful? We can caluclate whether two things (equations?) are equal rather than analytically solving them.

Proof. (by what method? by disproving the inverse)
Assume $a \ne b$.
Set $\epsilon = \frac{\| a - b\|}{2}$  <- what??? why, how?
... some algebra



# 313


# CS231n


# Prediction and learning

* The rate of learning is important. The resource we are tracking is mistakes. E.g. polynomial time algorithms, sub linear error!
* Computational complexity. Want is the minimum amount of errors that you have to make to learn a given data set.
* Experts = bandit (but with less info?) - partial information (like reinformcement learning)
  * Bandit, you have to explore.
* Upper connfidence bound (or UC tree) leads to? -> monte carlo tree search


# UMM

We define a memprocessor as an object defined by the four-tuple(x;y;z;)where x is the state of the memprocessor, y is the array of internal variables,z the array of variables that connect from one memprocessor to other memprocessors, and  an operator that defines the evolution
