---
layout: page
title:  "一个初学者眼中的动力系统"
subtitle: "低阶连续系统的基础概念"
date:   2025-1-21 01:00:00 +0530
categories: ["Analysis"]
lang: "zh"
---
# 动力系统简介

动力系统为研究**随时间变化**（动态）提供了一个数学框架。这篇博客旨在介绍用于分析一维和二维系统的基本概念和工具。

当我刚开始接触动力系统的时候，我感到非常困惑。我们已经有笛卡尔空间、偏微分方程（PDE）和常微分方程（ODE）来描述笛卡尔空间中的轨迹——那么为什么还需要**相空间**？笛卡尔空间还不够吗？

随着对动力系统的深入学习，我意识到仅使用笛卡尔空间来描述动态的局限性：它缺乏**时间信息**，也许这正是动力系统中“**动力**”一词的意义所在。

<img src="{{ "/assets/img/blog_25_1_21_1.jpg" | relative_url }}" alt="Alt text describing the image" style="width: 550px; height: auto; display: block; margin: auto;">

请看上图，显示了二维笛卡尔空间中的一条轨迹。一点从 $(x_0,y_0)$ 移动到 $(x_1,y_1)$。虽然我们可以看到点所经过的路径，但却无法得知点沿着这条路径移动的速度。单独的轨迹无法揭示系统的速度或其随时间的演变。

这正是**相空间**的重要性所在。通过转到**相空间**，我们不仅可以可视化系统的位置，还可以同时表示每一点的速度（或其他的物理量，取决于上下文）。例如，在**相空间**中，我们可以用 $x$ 和其速度 $v=\dot{x}$ 来表示系统的状态。这让我们能更清晰地观察整个系统随时间的演化。

**相空间**中的图 1 和图 2 说明了两个不同的运动方式可以在笛卡尔空间中共享相同的轨迹。

通过在每个位置可视化速度，**相空间**提供了一个更丰富、更完整的系统行为图景。它成为研究轨迹如何变化、识别**固定点**、**极限环**或混沌行为等模式以及理解系统整体动态的强大工具。

## 1. 一维流
让我们从一维系统开始。你可能会在动力系统中遇到的第一个不熟悉的符号是 $ \dot{x} $。但别担心，这只是 $\frac{dx}{dt}$ 的另一种表示方式。通常，我们将其表示为 $ \dot{x}= f(x) $，这意味着对于 $x$ 的每个值，系统都有一个对应的变化率 $\frac{dx}{dt}= f(x)$。例如，如果 $x$ 表示位置，那么 $ \dot{x}= f(x) $ 描述了该特定位置的速度。

### 1.1 固定点(fixed point)
- 定义：系统随时间不变化的点 $ \dot{x} = 0 $。
- 简单系统中固定点的示例，我们可以看到$x$轴上的箭头代表了该点的运动方向，因此这是为什么我们将**相空间**中的轨迹称之为**流**的原因，其本质是一个**向量场**，只不过在一维系统中只有两个方向因此感觉不是那么明显。
<img src="{{ "/assets/img/blog_25_1_21_2.png" | relative_url }}" alt="Alt text describing the image" style="width: 550px; height: auto; display: block; margin: auto;">

### 1.2 线性稳定性分析
这是一个非常有用的技巧，用于展开固定点附近的**流**，从而可以观察高阶项如何决定固定点附近的行为。
对于一般**流** $ \dot{x} = f(x) $，可以在任意固定点 $ x = x^* $ 附近求解。固定点的小偏差 $ \eta(t) = x(t) - x^* $ 化简如下：
$$
\dot{\eta} = \dot{x} - \frac{d}{dt} x^* = \dot{x} = f(x)
$$

将**流**展开到固定点的线性阶次：
$$
\dot{\eta} = f(x) = \underbrace{f(x^*)}_{=0} + f'(x^*) \underbrace{(x - x^*)}_{=\eta} + \frac{1}{2} f''(x^*) \underbrace{(x - x^*)^2}_{=\eta^2} + \cdots
$$

$$
\approx f'(x^*) \eta
$$

由于 $f(x^*) = 0 $（根据固定点的定义 $ \frac{d}{dt}x^\*=0 $），解为：
$$
\eta = \eta_0 e^{f'(x^*)t}
$$

**稳定性指数**：$\lambda = f'(x^*)$ 是稳定性指数，决定了固定点是稳定（$\lambda < 0$）还是不稳定（$\lambda > 0$）。

**注意！** 稳定性指数不是 $\lambda = \ddot{x}$。这是错误的，因为 $\ddot{x} = \frac{d^2 x}{dt^2}$，而稳定性指数是 $ \dot{x} $ 相对于坐标 $ x $ 的导数，即 $ \lambda \equiv \frac{\partial \dot{x}}{\partial x} $。

### 1.3 一维系统中的分岔理论
**什么是分岔？** 分岔是动力系统随**参数**变化而发生的系统性的改变。想象一个重物放在一根杆子上。当箱子的重量改变时，杆子平衡时候的弯曲度也会改变。然而，如果我们不断增加箱子的重量，当重量超过杆子可以承受的重量之后，杆子就会断裂。这个断裂点表示箱-杆系统的一个**分岔**：在这个点之后，无论箱子的重量如何，杆都无法恢复到任何稳定状态的弯曲度。
<img src="{{ "/assets/img/blog_25_1_21_13.png" | relative_url }}" alt="Alt text describing the image" style="width: 650px; height: auto; display: block; margin: auto;">

- **单参数分岔**：
  - 鞍结分岔(saddle node bifurcation)。
  - 横贯分岔(transcritical bifurcation)。
  - Pitchfork 分岔（超临界和亚临界）。
<img src="{{ "/assets/img/blog_25_1_21_3.png" | relative_url }}" alt="Alt text describing the image" style="width: 650px; height: auto; display: block; margin: auto;">

- **双参数分岔**：
  - 在具有两个参数 $r$ 和 $s$ 的系统中，$ \dot{x} = f(x, r, h)$，固定点形成一个曲面
$x^*(r, h)$，曲面上的所有点是 $\dot{x}=0$ 的地方，因此这个曲面也称为**平衡流形**，而分岔发生在曲线 $h_c (r)$ 处。
<img src="{{ "/assets/img/blog_25_1_21_4.png" | relative_url }}" alt="Alt text describing the image" style="width: 650px; height: auto; display: block; margin: auto;">
  - **突变**(catastrophe)：参数的微小变化可能导致系统平衡状态的显著变化。
  - **滞后现象**(hysteresis)：在 $xoh$ 平面中的环状结构被称为**滞后环**(hysteresis loop)。在 $h_c$ 附近微小的 $h$ 改变可能导致显著的平衡状态变化，而如果系统希望回到之前的平衡状态，$h$ 必须先调整到 $-h_c$，然后再缓慢返回 $h_c$。

## 2. 平面上的流
平面上的**流**比一维**流**更为有趣，因为它展现了更丰富的全局结构。除了单一的固定点，还可能出现诸如**闭轨道(closed orbits)**、**极限环(limit cycles)**（孤立的闭轨道）、**同宿轨道(homoclinic orbits)**或**异宿轨道(heteroclinic orbits)**等现象。

### 2.1 二维系统中的固定点
- 使用**线性稳定性分析**分类：对于二维系统，我们首先确定其**雅可比矩阵**。在我们想分析的固定点附近，我们通过线性近似研究该点附近的运动趋势。

固定点可以分类如下：
  - 稳定/不稳定螺旋。
  - 稳定/不稳定节点。
  - 中心。
  - 退化点。

通过参考固定点的分类图，我们可以通过雅可比矩阵的**迹**和**行列式**快速确定固定点的类型。
<img src="{{ "/assets/img/blog_25_1_21_5.png" | relative_url }}" alt="Alt text describing the image" style="width: 500px; height: auto; display: block; margin: auto;">

对于一个二维系统：
$$\dot{x} = Ax \, , \, A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \, .$$  
根据特征方程 $0 = \det(A - \lambda I) = \lambda^2 - \tau\lambda + \Delta$，我们可以得到系统的特征值。

为什么我们关心系统的**特征值**？因为它们使我们能够将系统变换到特征向量张成的空间。这简化了分析，我们可以专注于特征值如何决定系统在固定点附近的行为。如果特征值的**实部**大于 0，系统将在相应的特征向量方向上指数增加。相反，如果特征值的**实部**小于 0，系统将在该方向上指数收缩。

下方的证明表明，特征值在解轨迹中充当指数因子，解释了指数扩展和收缩的来源。

<p style="text-align: center;">
    $$  \dot{x}=Ax = PDP^{-1}x \\ \Rightarrow \frac{d}{dt}[P^{-1}x] = D \underbrace{P^{-1}x}_{\xi} \\\Rightarrow \dot{\xi} = D\xi \\ \Rightarrow \xi(t) = \begin{pmatrix} e^{\lambda_1 t} \xi_1(0) \\ e^{\lambda_2 t} \xi_2(0) \end{pmatrix}$$
</p>

当我第一次学习这一点时，我感到迷惑的点是为什么 0 是阈值而不是 1。我最初认为反复将矩阵应用于一个给定向量会使该向量在 $\|\lambda\|>1$ 的方向上增长，而在 $\|\lambda\|<1$ 的方向上收缩。

我的误解是源于矩阵并不是直接应用于物理实体，而是作用在**相空间**中，特别是对 ODE 系统。当我们求解 ODE 系统以获得解时，$\lambda$ 表示指数而不是乘数因子！

而当特征值为复数时，**振荡现象出现了！**，解的形式如下：
$$\xi(t) = \xi_1(0) e^{\mu t} \begin{pmatrix} \cos(\omega t) \\ \sin(\omega t) \end{pmatrix}$$
其中 $\mu$ 是特征值的实部，$\omega$ 是其虚部。

### 2.2 非局部结构
到目前为止，我们仅讨论了系统在特定点（即固定点）周围的局部行为。然而，在二维系统中，还会出现**新结构**，例如**闭轨道**和**极限环**。

- **哈密顿系统中的闭轨道**：
  - 守恒定律导致**闭轨道**的出现。
  - 像这样的简单**哈密顿系统**可以在**相空间**平面中形成闭轨道。想象围绕中心的一组闭轨道，这些轨道表示在相同的起始位但是拥有不同的初始速度。
    <img src="{{ "/assets/img/Simple_Harmonic_Motion_Orbit.gif" | relative_url }}" alt="Alt text describing the image" style="width: 500px; height: auto; display: block; margin: auto;">
  - **哈密顿系统**的数学形式如下：
    <p style="text-align: center;">
      $$ H \equiv \frac{p^2}{2m} + V(x) \\ \dot{x} = \frac{\partial H}{\partial p} = \frac{p}{m} \\ \dot{p} = -\frac{\partial H}{\partial x} = -\frac{\partial V}{\partial x} \\$$
    </p>

    这里，$x$ 通常表示位置，而 $p$ 表示动量，定义为 $p=mv$。因此，总能量 $E=H(x,p)$ 是守恒的，因为 $\dot{H}=0$，即总能量随时间不会改变。
    <p style="text-align: center;">
      $$\dot{H} = \frac{\partial H}{\partial x} \underbrace{\dot{x}}_{\frac{\partial H}{\partial p}} + \frac{\partial H}{\partial p} \underbrace{\dot{p}}_{-\frac{\partial H}{\partial x}} = 0.$$
    </p>

- **极限环**：

  在没有对称性的系统中，闭轨道的带状结构是罕见的，因为非线性通常会破坏这种完美的对称结构。然而，孤立的闭轨道（即**极限环**）仍然可能通过振荡的方式出现。

  使用极坐标分析圆形结构通常更容易，典型的表示如下：
  <img src="{{ "/assets/img/blog_25_1_21_6.png" | relative_url }}" alt="Alt text describing the image" style="width: 500px; height: auto; display: block; margin: auto;">

  - 如何找到极限环：
    - **庞加莱-本迪克森定理**：假设在平面中存在一个光滑的、有界的区域 $D$。进一步假设 $D$ 中不包含任何固定点，并且存在一条始终局限于 $D$ 的轨迹。那么在 $D$ 中至少存在一个周期轨道。
      <img src="{{ "/assets/img/blog_25_1_21_7.png" | relative_url }}" alt="Alt text describing the image" style="width: 500px; height: auto; display: block; margin: auto;">

  - 如何排除闭轨道或极限环：
    - **梯度系统**：$\dot{x} = - \nabla V(x)$，在梯度系统中，$x$ 总是朝着使总能量 $V$ 最快减少的方向移动，因此不会出现振荡。
    - **Dulac 判据**：考虑一个可微函数 $V(x)$，使得 $\nabla \cdot (V\dot{x})$ 在某个区域内不改变符号。如果这样的函数存在，则该区域内没有闭轨道（格林定理）。
    - **指数理论**：极限环的**指数**始终为 +1。因此，如果某条**闭曲线**的指数为 −1，并且我们可以确认该区域内仅存在一个固定点，则可以明确排除区域内存在极限环的可能性。（这只是排除极限环的众多规则之一。）

### 2.3 极限环的分岔

- **极限环的鞍结分岔**：只需改变参数 $r$，极限环就会在相空间中出现！
  <img src="{{ "/assets/img/blog_25_1_21_8.png" | relative_url }}" alt="Alt text describing the image" style="width: 500px; height: auto; display: block; margin: auto;">
- **SNIPER（鞍结无限周期）分岔**：调整角速度 $\omega$，直到某一点固定点恰好出现在极限环上。
  <img src="{{ "/assets/img/blog_25_1_21_9.png" | relative_url }}" alt="Alt text describing the image" style="width: 500px; height: auto; display: block; margin: auto;">
- **同宿分岔**：极限环与鞍点发生碰撞！
  <img src="{{ "/assets/img/blog_25_1_21_10.png" | relative_url }}" alt="Alt text describing the image" style="width: 500px; height: auto; display: block; margin: auto;">

### 2.4 平面分岔
除了相空间中极限环的分岔外，二阶系统中还可以出现另一种类型的分岔，即**Hopf 分岔**。
- **Hopf 分岔**：
  - 超临界 Hopf 分岔：可以被直观地看作一个极限环从固定点“长出来”。这种类型的分岔发生在因为参数变化而导致稳定点从分类在$\Delta - \tau $图中发生变化（详见第 2.1 节）。
    <img src="{{ "/assets/img/blog_25_1_21_11.png" | relative_url }}" alt="Alt text describing the image" style="width: 500px; height: auto; display: block; margin: auto;">

### 2.5 指数理论
**庞加莱指数(Index)**
- **庞加莱指数**介绍：
  - 任意**闭合的**、**不相交的**曲线 $C$（不穿过任何固定点）的指数，定义为我们逆时针绕曲线 $C$ 一圈时向量场的圈数，可以想象拿着一支笔，逆时针围绕着曲线$C$运动，而笔尖的朝向时刻与向量场中的方向重合，在环绕一圈后，笔尖逆时针转动的圈数就是该曲线的指数（一个有意思的场景，考试的时候大家都在转笔，其实是在计算Index哈哈哈）：
    <img src="{{ "/assets/img/blog_25_1_21_12.png" | relative_url }}" alt="Alt text describing the image" style="width: 500px; height: auto; display: block; margin: auto;">
  - 我们还可以通过解析方法求解，但需要注意：$\varphi =\text{atan} \left( \frac{\dot{y}}{\dot{x}} \right)$，而不是 $\varphi =\text{atan} \left( \frac{y}{x} \right)$。这种区别在于我们积分的是流方向的角度，而不是坐标本身，这是一个很容易犯的错误！！
    <p style="text-align: center;">
      $$\varphi = \text{atan} \left( \frac{\dot{y}}{\dot{x}} \right) = \text{atan} \left( \frac{g(x,y)}{f(x,y)} \right)\\
      \text{d}\varphi = \frac{\partial \varphi}{\partial f} \text{d}f + \frac{\partial \varphi}{\partial g} \text{d}g = -\frac{g}{f^2 + g^2} \text{d}f + \frac{f}{f^2 + g^2} \text{d}g \\

      \Rightarrow I_C \equiv \frac{\Delta \varphi}{2\pi} = \frac{1}{2\pi} \oint_C \text{d}\varphi = \frac{1}{2\pi} \oint_C \frac{f \text{d}g - g \text{d}f}{f^2 + g^2}$$
    </p>

- 重要性质：
  - 未包含任何固定点的曲线 $C$ 的指数为 $I_C = 0$。
  - 将向量场的所有箭头反向（$t \to -t$）不改变指数。
  - 闭轨道的指数（即曲线 $C$ 和闭轨道重合）为 $I_C = +1$。
  - 包围 $N$ 个孤立固定点的曲线 $C$ 的指数为 $I_C = I_1 + I_2 + · · · + I_N$。
  - ...

## 结语
这篇博客仅覆盖了动力系统非常非常小的一部分基础内容，这个领域确实很有意思但是也非常有挑战性。为了理解这些概念并准备考试，我花费了大量时间！以后如果有机会在这个领域进一步学习或工作，我希望能够分享下更高级主题的内容，例如混沌、奇异吸引子、分形等等。

## Key takeaways
- **一维流**：
  - 固定点。
  - 线性稳定性分析。
  - 分岔理论：鞍结分岔、横贯分岔、Pitchfork 分岔。

- **平面上的流**：
  - 固定点的分类：稳定/不稳定螺旋、稳定/不稳定节点、中心。
  - 非局部结构：
    - 哈密顿系统中的闭轨道。
    - 极限环：极限环的分岔。
  - 指数理论。

## References
- *TIF155 / FIM770 Dynamical Systems Course Lecture Notes, Chalmers University of Technology*
- *Nonlinear Dynamics and Chaos_ With Applications to Physics, -- Steven H_ Strogatz -- Studies in Nonlinearity, 2, 2014*
