---
layout: page
title:  "A Beginner's Perspective on Dynamical Systems"
subtitle: ""
date:   2025-1-21 01:00:00 +0530
categories: ["Analysis"]
lang: "en"
---
# Introduction to Dynamical Systems

Dynamical systems provide a mathematical framework to study how things change **over time**(dynamical). This blog aims to introduce the basic concepts and tools used to analyze 1-dimensional and 2-dimensional systems. 


When I first encountered dynamical systems, I was incredibly confused. We already have Cartesian space, partial differential equations (PDEs), and ordinary differential equations (ODEs) to describe trajectories in Cartesian space—so why do we need **phase space**? Isn't Cartesian space enough?

As I delved deeper into the subject, I realized the limitation of describing dynamics solely in Cartesian space: it lacks **temporal information**, and maybe this is where the word **dynamical** stands for.

<img src="{{ "/assets/img/blog_25_1_21_1.jpg" | relative_url }}" alt="Alt text describing the image" style="width: 550px; height: auto; display: block; margin: auto;">


Consider the figure above, which shows a trajectory in 2D Cartesian space. A point moves from $(x_0,y_0)$ to $(x_1,y_1)$. While we can see the path the point takes, we have no way to tell how fast it moves along that path. The trajectory alone doesn’t reveal the system’s velocity or how it evolves over time.

This is where phase space becomes essential. By transitioning to phase space, we can visualize not only the position of the system but also its velocity (or momentum, depending on the context) at every point. For instance, in phase space, we can represent a system’s state using both $x$ and its velocity $  v=\dot{x}  $ .This allows us to observe how the dynamics evolve over time with greater clarity.

Figures $ 1 $ and $2$ in phase space illustrate that two different dynamics can share the same trajectory in Cartesian space.

By visualizing the velocity at each position, phase space provides a richer, more complete picture of the system’s behavior. It becomes a powerful tool for studying how trajectories change, identifying patterns like fixed points, limit cycles, or chaotic behavior, and understanding the system’s overall dynamics.


## 1. One-Dimensional Flow
Let’s begin with a one-dimensional system. The first unfamiliar notation you’ll likely encounter in dynamical systems is $ \dot{x}  $. But don’t worry—it’s simply another way of writing $\frac{dx}{dt}$. Typically, we express this as $ \dot{x}= f(x)  $, which means that for every value of $x$, the system has a corresponding rate of change $\frac{dx}{dt}= f(x)$. For example, if $x$ represents position, then $ \dot{x}= f(x)  $ describes the velocity at that specific position.

### 1.1 Fixed Points
- Definition: Points where the system does not change over time $ \dot{x} = 0 $. 
- Examples of fixed points in simple systems.
<img src="{{ "/assets/img/blog_25_1_21_2.png" | relative_url }}" alt="Alt text describing the image" style="width: 550px; height: auto; display: block; margin: auto;">

### 1.2 Linear stability analysis
This is a very useful technique to expand the flow around fixed point, so that we can observe how higher order term dictates the dynamic around the fixed point.
A general flow $ \dot{x} = f(x) $ can be solved close to any fixed point $ x = x^* $.  A small deviation $ \eta(t) = x(t) - x^* $ from $ x^* $ evolves according to  
$$
\dot{\eta} = \dot{x} - \frac{d}{dt} x^* = \dot{x} = f(x)
$$

Series expand the flow around the fixed point to linear order:  
$$
\dot{\eta} = f(x) = \underbrace{f(x^*)}_{=0} + f'(x^*) \underbrace{(x - x^*)}_{=\eta} + \frac{1}{2} f''(x^*) \underbrace{(x - x^*)^2}_{=\eta^2} + \cdots
$$

$$
\approx f'(x^*) \eta
$$

where  $f(x^*) = 0 $ ($ \frac{d}{dt}x^\*=0 $)  accordingto the definition of a fixed point. Solution:
$$
\eta = \eta_0 e^{f'(x^*)t}
$$

**stability exponent**: $\lambda = f'(x^*)$ is the stability exponent,It determines whether the fixed point is stable (λ < 0) or unstable (λ > 0).

**be careful!** the stability exponent is not  $\lambda = \ddot{x}$ . This is incorrect because it means$ \ddot{x} = \frac{d^2 x}{dt^2} $, while the stability exponent is the derivative of $ \dot{x} $ with respect to the coordinate $ x $, $ \lambda \equiv \frac{\partial \dot{x}}{\partial x} $.


### 1.3 Bifurcations in 1D
**What is bifurcation?** A bifurcation is a qualitative change in the dynamics of a system as a **parameter** is varied. Imagine a box resting on a pole. As the weight of the box changes, the curvature of the pole also changes to balance the system. However, if we keep increasing the weight of the box, there may come a point where the pole breaks. This breaking point represents a bifurcation in the box-pole system: beyond this point, the pole can no longer return to any stable curvature, regardless of the weight of the box.

- **One-Parameter Bifurcations**:
  - Saddle-node bifurcation.
  - Transcritical bifurcation.
  - Pitchfork bifurcation (supercritical and subcritical).
<img src="{{ "/assets/img/blog_25_1_21_3.png" | relative_url }}" alt="Alt text describing the image" style="width: 650px; height: auto; display: block; margin: auto;">

- **Two-Parameter Bifurcations**:
  - In systems with two parameters $r$ and $s$,$ \dot{x} = f(x, r, h)$ , fixed points form surfaces
$x^*(r, h)$all the points on the surface are where $\dot{x}=0$ so the surface also called **equilibrium manifold** , and bifurcations occur at curves $h_c (r)$. when $h=0$ we can imagine on $xor$ (in the plot the $u$ should be $x$ here, never mind≧▽≦) plane will form a supercritical pitchfork, and when $r>0$ there will be 3 fixed points.
<img src="{{ "/assets/img/blog_25_1_21_4.png" | relative_url }}" alt="Alt text describing the image" style="width: 650px; height: auto; display: block; margin: auto;">
  - **catastrophe**:A small change in a parameter that causes a significant change in the equilibrium state of a system.
  - **hysteresis**: The loop in the $xoh$ plane is called **hysteresis loop**, a small change of $h$ near $h_c$ will lead to a drastic change of equilibrium state, and if the system want to return to the equilibrium state before, $h$ should be adjust to $-h_c$ and then slowly adjust back to $h_c$.

## 2. Flow on the Plane

### 2.1 Fixed Points in 2D
- Classification using **Linear Stability Analysis**:
  - Stable/unstable spiral.
  - Stable/unstable node.
  - Center.
- Eigenvalue-based stability criteria.

### 2.2 Non-Local Structures
- **Closed Orbits in Hamiltonian Systems**:
  - Conservation laws leading to closed orbits.
- **Limit Cycles**:
  - Definition: Isolated closed trajectories in phase space.
  - Examples of systems exhibiting limit cycles (e.g., Van der Pol oscillator).
  - How to rule out or find limit cycles:
    - **Poincaré-Bendixson Theorem**.
    - Dulac’s criterion.
  - Techniques to locate limit cycles:
    - Numerical simulations.
    - Perturbation methods.

### 2.3 Bifurcations of Limit Cycles
- Saddle-node bifurcation of limit cycles.
- SNIPER (Saddle-Node Infinite Period) bifurcation.
- Homoclinic bifurcation.

### 2.4 Planar Bifurcations
- **Hopf Bifurcation**:
  - Supercritical and subcritical Hopf bifurcations.
- Relationship between fixed points and the onset of oscillatory behavior.

### 2.5 Index Theory
- Introduction to the **Poincaré Index**:
  - Index of fixed points and its interpretation.
  - Applications to determine the global behavior of a system.
- Index Theorem:
  - Relationship between the sum of indices and system topology.

---

## Conclusion

Dynamical systems offer a rich set of tools to analyze time-dependent phenomena across disciplines. From fixed points to limit cycles and bifurcations, understanding the local and global behavior of a system is essential for grasping its dynamics. This blog provided an overview of the fundamental concepts in 1D and 2D flows, equipping you with the foundation to explore more advanced topics.

---

## References
- Suggested textbooks or papers for further reading.
- Links to online simulations or interactive tools for dynamical systems.


