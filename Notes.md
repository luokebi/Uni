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

#### Geometric series

$ 1 + 1/2 + 1/4 + 1/8 + \dots $ converges to 2. 
$\sum_{k=0}^\infty ar^k = \frac{a}{1-r} - 0 = \frac{a}{1-r} = \frac{1}{1-\frac{1}{2}} = 2$
So the next term to be added decreases faster than the infinity of added terms? Weird!!

# 313

Does an open set have to be continuious? Define continuoius in this circumstance? We can continuiously go between integers, even though they are discrete???

### Definition of a topological space
The empty set and X itself belong to τ.
Any (finite or infinite) union of members of τ still belongs to τ.
The intersection of any finite number of members of τ still belongs to τ.

The definition of a topological space reminds me of a group?!?
The set X, under the operation Union, is ... must be a closure in X. Associative, commutative, ... inverse = ??,  Identity = {}.

$\mathcal{T} = \{A \subseteq X \mid A=\varnothing \mbox{ or } X \setminus A \mbox{ is finite} \}$

A is open if (R - A) is finite.(Cofinite) Doesnt make any sense to me? 
As if A = (0,1) then (R-A) = [-\infty,0],[1,\infty] ???

### Neighourhood

If A is a subset from a topological space T that contains a point p, we can say that p is in the neighbourhood of A.

# CS231n


# Prediction and learning

* The rate of learning is important. The resource we are tracking is mistakes. E.g. polynomial time algorithms, sub linear error!
* Computational complexity. Want is the minimum amount of errors that you have to make to learn a given data set.
* Experts = bandit (but with less info?) - partial information (like reinformcement learning)
  * Bandit, you have to explore.
* Upper connfidence bound (or UC tree) leads to? -> monte carlo tree search


# UMM

Why define a state and internal variables seperately? 
* This shit seems important! Very similar to how quantum computers are supposed to work?
 * Could I implement something like Shors algorithm on one??? That sounds like an interesting project.
* To - do. Simulate the dynamical equations for a 1, 2/3 memprocessor system.
