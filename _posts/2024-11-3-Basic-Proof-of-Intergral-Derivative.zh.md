---
layout: page
title:  "微积分基本定理"
subtitle: "微积分基本定理的直观证明"
date:   2024-11-03 10:21:21 +0530
categories: ["Analysis"]
lang: "zh"
---

你是否曾经疑惑，为什么积分的导数能够回到原函数？这个联系是微积分基本定理的核心，它优雅地将微分和积分这两个微积分的中心概念结合在一起。

## 问题
<p style="text-align: center;">
  $\frac{d}{dx} \int_0^x f(t) \, dt = f(x) \, $
</p>

一般也会写成
<p style="text-align: center;">
  $\frac{dF(x)}{dx} = f(x) \, $   其中
  $F(x) = \int_0^x f(t) \, dt$
</p>

为了证明这一点，我们将使用导数的 **基本定义**，并利用**积分均值定理**。


## 逐步证明
让我们首先定义函数 $F(x) = \int_0^x f(t) , dt$。我们希望求出 $F(x)$ 对 $x$ 的导数。简单地重写 $F(x)$ 的导数定义，我们得到：
<p style="text-align: center;">
  $\frac{d}{dx} \int_0^x f(t) \, dt = \lim_{\Delta x \to 0} \frac{\int_0^{x+\Delta x} f(t) \, dt - \int_0^x f(t) \, dt}{\Delta x}$
</p>

上面的表达式可以根据**定积分的加法性质**来简化。根据这个性质，如果我们有一个区间，我们可以将该区间的积分分成两个部分：

<p style="text-align: center;">
  $= \lim_{\Delta x \to 0} \frac{\int_0^x f(t) \, dt + \int_x^{x+\Delta x} f(t) \, dt - \int_0^x f(t) \, dt}{\Delta x}$
</p>

<p style="text-align: center;">
  $= \lim_{\Delta x \to 0} \frac{\int_x^{x+\Delta x} f(t) \, dt}{\Delta x}$
</p>

根据**积分的均值定理**，对于在区间上的连续函数，存在某个点使得：

<p style="text-align: center;">
  $\int_a^b f(t) \, dt = f(c) \cdot (b-a)$
</p>

而在我们的例子中:
<p style="text-align: center;">
    $\int_x^{x+\Delta x} f(t) \, dt = f(c) \cdot \Delta x$
</p>

其中 $c$ 是 $x$ 和 $x + \Delta x$ 之间的某个点。当 $\Delta x \to 0$ 时，$c \to x$。因此，我们可以将上述表达式重写为：

<p style="text-align: center;">
  $= \lim_{\Delta x \to 0} \frac{f(x) \cdot \Delta x}{\Delta x} = f(x)$
</p>

<!-- <p style="text-align: center;">
  $= f(x)$
</p> -->

## Key Takeaways
一些更加直观的感受
- $F(x)$ 对应于微小变化 $\Delta x$ 的变化量是 $f(x) \cdot \Delta x$。
- 然后我们除以 $\frac{f(x) \cdot \Delta x}{\Delta x}$，以求得 $F(x)$ 相对于 $x$ 的变化率。
- 这个变化率恰好是 $f(x)$，这就是为什么积分的导数能够回到原函数的原因。



