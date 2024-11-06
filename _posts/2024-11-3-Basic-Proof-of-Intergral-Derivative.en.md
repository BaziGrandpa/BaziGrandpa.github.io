---
layout: page
title:  "Fundamental Theorem of Calculus"
subtitle: "My understanding of the Fundamental Theorem of Calculus: A Step-by-Step Proof Explained"
date:   2024-11-03 10:21:21 +0530
categories: ["Analysis"]
lang: "en"
---

Have you ever wondered why the derivative of an integral gives back the original function? This connection lies at the heart of the Fundamental Theorem of Calculus, which beautifully ties together differentiation and integration—the two central concepts of calculus. In this blog post, I'll take you through an intuitive proof that demonstrates why:

## The Problem Statement
<p style="text-align: center;">
  $\frac{d}{dx} \int_0^x f(t) \, dt = f(x) \, $
</p>

and sometimes written as
<p style="text-align: center;">
  $\frac{dF(x)}{dx} = f(x) \, $   where
  $F(x) = \int_0^x f(t) \, dt$
</p>
To do this, we'll use the definition of a derivative and leverage the Mean Value Theorem for integrals.


## Step-by-Step Proof
Let's start by defining the function $F(x) = \int_0^x f(t) \, dt$. We want to find the derivative of $F(x)$ with respect to $x$. Just simply rerwrite the definition of the derivative of $F(x)$, we get
<p style="text-align: center;">
  $\frac{d}{dx} \int_0^x f(t) \, dt = \lim_{\Delta x \to 0} \frac{\int_0^{x+\Delta x} f(t) \, dt - \int_0^x f(t) \, dt}{\Delta x}$
</p>

The above expression can be simplified by breaking down the difference of the integrals

This simplification works because of the **additive property of definite integrals**. According to this property, if we have an interval , we can split the integral over that interval into two parts. Specifically:

<p style="text-align: center;">
  $= \lim_{\Delta x \to 0} \frac{\int_0^x f(t) \, dt + \int_x^{x+\Delta x} f(t) \, dt - \int_0^x f(t) \, dt}{\Delta x}$
</p>

<p style="text-align: center;">
  $= \lim_{\Delta x \to 0} \frac{\int_x^{x+\Delta x} f(t) \, dt}{\Delta x}$
</p>

According to the **Mean Value Theorem for Integrals**, for a continuous function over the interval , there exists some point such that:

<p style="text-align: center;">
  $\int_a^b f(t) \, dt = f(c) \cdot (b-a)$
</p>

In our case, we have:
<p style="text-align: center;">
    $\int_x^{x+\Delta x} f(t) \, dt = f(c) \cdot \Delta x$
</p>

where $c$ is some point between $x$ and $x + \Delta x$. And $\Delta x \to 0$, so $c \to x$. Therefore, we can rewrite the above expression as:

<p style="text-align: center;">
  $= \lim_{\Delta x \to 0} \frac{f(x) \cdot \Delta x}{\Delta x} = f(x)$
</p>

<!-- <p style="text-align: center;">
  $= f(x)$
</p> -->

## Key Takeaways
- the corresponding change of $F(x)$ respects the tiny change $\Delta x$ is $f(x) \cdot \Delta x$
- and then we divide by $\frac{f(x) \cdot \Delta x}{\Delta x} $ to get the rate of change of $F(x)$ with respect to $x$. 
- This rate of change is precisely $f(x)$. This is why the derivative of an integral gives back the integrand function.



