---
layout: page
title:  "Numerical PDEs"
subtitle: ""
date:   2025-4-4 01:00:00 +0530
categories: ["Numerical Analysis"]
lang: "en"
---

# Bridging the Gap: From Continuous PDEs to Finite Difference Methods

In computational mathematics, we often face partial differential equations (PDEs) that are difficult — or impossible — to solve analytically. To approach these problems, we turn to **numerical methods** like the **finite difference method (FDM)**.

But how do we ensure that these discrete approximations actually behave like the original equation? That’s where key ideas like **grid projection**, **residual**, **consistency**, and **stability** come into play.

---

## 🌉 From Continuous to Discrete: Building the Bridge

We begin with a general PDE:

$$
Lu = f
$$

Where:
- $u(x, t)$ is the **unknown solution** in continuous space,
- $f(x, t)$ is the **source term**,
- $L$ is a differential operator (like $\frac{\partial^2}{\partial x^2}$ or $\frac{\partial u}{\partial t}$).

To solve this numerically, we define a **discrete grid** over space and time:

$$
x_m = x_0 + mh, \quad t_n = t_0 + n\tau
$$

Here:
- $h$ is the space step size,
- $\tau$ is the time step size,
- $m, n \in \mathbb{Z}$ index the grid in space and time.

The **grid projection** of a continuous function like $u$ or $f$ is:

$$
u_{\tau h} = u(x_m, t_n), \quad \phi_{mn} = f(x_m, t_n)
$$

The function $y_{mn}$, defined only at discrete points, is called a **grid function**, and it approximates the continuous solution: $y_{mn} \approx u(x_m, t_n)$.

---

## 🧮 Discretizing the PDE: The Finite Difference Scheme

We now discretize the operator $L$ to form a **finite difference operator**, which we'll also call $L$ by convention. This gives us the discrete version of the PDE:

$$
Ly = \phi
$$

This is an algebraic system that we can solve numerically. But how do we know if this system faithfully represents the original PDE?

---

## 📏 Residual: Testing the Scheme

To test how well our finite difference method approximates the PDE, we define the **residual**:

$$
r_{\tau h} = L u_{\tau h} - \phi
$$

This measures the **discrepancy** between the finite difference scheme and the exact solution, evaluated on the grid.

If the method is good, this residual should become small as the grid is refined.

---

## ✅ Definition: Consistency

A finite difference method is called **consistent** with the original PDE if the residual tends to zero as the grid is refined:

$$
\|r_{\tau h}\| \to 0 \quad \text{as} \quad h, \tau \to 0
$$

Here, $\|\cdot\|$ is a suitable norm (e.g. $L^2$, $L^\infty$) over the space of grid functions.

**Intuition:** Consistency checks if your scheme **captures the dynamics** of the original PDE correctly.

---

## 🛡️ Definition: Stability (Zero-Stability)

Stability ensures that **small perturbations** in input data or the right-hand side do **not lead to large errors** in the numerical solution.

Formally, the method is **stable** if, for two problems with perturbed right-hand sides:

$$
Ly^{(1)} = f + \varepsilon^{(1)}, \quad Ly^{(2)} = f + \varepsilon^{(2)},
$$

the solutions satisfy:

$$
\|y^{(1)} - y^{(2)}\| \leq C \left( \|\varepsilon^{(1)}\| + \|\varepsilon^{(2)}\| \right)
$$

for a constant $C$ independent of $h, \tau$, and for small enough perturbations.

**Intuition:** Stability asks whether the method is **sensitive to noise or rounding errors**. A stable method won’t "explode" due to small mistakes.

---

## 📚 The Big Picture: Lax Equivalence Theorem

If a finite difference method is **consistent** and **stable**, then it is **convergent**.

That is:

$$
y_{mn} \to u(x_m, t_n) \quad \text{as} \quad h, \tau \to 0
$$

This tells us the numerical solution truly approximates the continuous one.

---

## 🧠 Intuition Recap

| Concept      | What it means                      | Why it matters                            |
|--------------|------------------------------------|--------------------------------------------|
| **Grid projection** | Sample continuous functions on a discrete grid | Bridge between continuous and discrete |
| **Consistency**     | Scheme matches PDE as grid refines         | Are we solving the right problem?         |
| **Stability**       | Errors stay under control                  | Will it explode?                          |
| **Convergence**     | Numerical solution approaches the true one | End goal: correctness                     |

---

## 🔍 How to Prove Stability?

Here are common methods used to prove stability:

### 🔸 Matrix Norms (for linear systems)

For a system $Ay = b$, prove:

$$
\|A^{-1}\| \leq C
$$

### 🔸 Von Neumann Analysis (for time-dependent PDEs)

1. Assume a Fourier mode solution: $y^n_m = G^n e^{ikmh}$
2. Solve for the amplification factor $G$
3. Show $\|G\| \leq 1$ for all $k$

### 🔸 Energy Methods

Construct a discrete inequality like:

$$
\|y^{n+1}\| \leq \|y^n\| + \text{(controlled terms)}
$$

### 🔸 Maximum Principles

Use convex combinations of past values to show:

$$
\|y^{n+1}\|_\infty \leq \|y^n\|_\infty
$$

---

## 🎯 Final Thoughts

Understanding how finite difference methods transition from the continuous world to the discrete is **crucial** for building reliable numerical solvers. You now know:

- How continuous PDEs are discretized via grid projection,
- How to define and interpret residual, consistency, and stability,
- And how to begin proving that your method behaves well.

A good scheme must be **consistent**, **stable**, and therefore **convergent**. Without all three, your numerical answers might be fast — but they won’t be right.

---

*Written with curiosity and appreciation for beautiful math 💻✨*

