---
layout: page
title:  "拉格朗日乘数法的几何解释"
subtitle: 
date:   2024-11-07 19:46:21 +0530
categories: ["Stochastic Optimization"]
lang: "zh"
---

优化问题在工程、经济和科学中至关重要。通常，我们需要在一个约束条件下优化一个函数。**拉格朗日乘数法**为解决这样的**约束优化**问题提供了一种有效的方法。

## 什么是拉格朗日乘数法？以2维为例

假设我们希望最小化（或最大化）一个函数 $f(x_1, x_2)$，但必须满足一个约束条件 $g(x_1, x_2) = 0$。**拉格朗日乘数法**使我们能够同时考虑目标函数和约束条件。

### 几何上的概念
<img src="{{ "/assets/img/blog_24_11_07_1.jpg" | relative_url }}" alt="描述图片的替代文字" style="width: 500px; height: auto; display: block; margin: auto;">

为了在约束 $g(x_1, x_2) = 0$ 下最小化 $f(x_1, x_2)$，我们需要确保在最优点处，$f$ 的梯度（$\nabla f$）与 $g$ 的梯度（$\nabla g$）**平行**。这意味着两个梯度指向相同(或者相反)的方向[（梯度和函数变化的关系）]({% post_url 2024-11-06-why-gradiant-is-the-steepest-directoin.zh %})，表明在不违反约束的情况下，没有进一步的优化的空间。数学上可以表示为：

$$
\nabla f = \lambda \nabla g
$$

并将其转换为以下方程组：

$$
\begin{cases}
\frac{\partial f}{\partial x_1} + \lambda \frac{\partial g}{\partial x_1} = 0 \\
\frac{\partial f}{\partial x_2} + \lambda \frac{\partial g}{\partial x_2} = 0 \\
g(x_1, x_2) = 0
\end{cases}
$$

其中，$\lambda$ 是拉格朗日乘数，表示梯度之间的比例关系。在最优点处，沿着约束条件的任何移动都会改变 $f$ 的值，这种变化将使得该值不再是最优，表明当前点是在给定条件下的最佳解。

## 可视化
<img src="{{ "/assets/img/blog_24_11_07_2.jpg" | relative_url }}" alt="描述图片的替代文字" style="width: 500px; height: auto; display: block; margin: auto;">

- **目标函数**：函数 $f(x_1, x_2) = x_1^2 + x_2^2$ ，目标是找到这个曲面上的最低点。

- **约束条件**：约束条件 $g(x_1, x_2) = x_1 + x_2 - 1 = 0$ 在$x_1x_2$平面是一条直线。解必须位于这条直线上。

- **梯度对齐**：在最优点处，$f$ 的梯度与 $g$ 的梯度是平行的。

当梯度不对齐时，我们可以将 $f$ 的梯度分解为两个部分：**一个平行于约束直线**，**另一个垂直于约束直线**。如果我们沿着约束移动，$f$ 的值将会改变，更具体地说，在这种情况下会减少。正如我们在[之前的文章]({% post_url 2024-11-06-why-gradiant-is-the-steepest-directoin.zh %})中提到的，梯度方向是**最陡增幅**的方向，因此分解的**相反方向**将是最陡减少的方向。因此，沿着约束移动将减少 $f$ 的值，表明当前点不是最优的。

## Key Takeaways

- 拉格朗日乘数法通过确保目标函数与约束之间的梯度**平行**，从而找到最优解。
- 如果梯度不对齐，我们可以将目标函数的梯度分解为**沿约束方向**和**垂直约束方向**。沿约束移动将减少（或者增加） $f$ 的值，表明当前点不是最优的。


