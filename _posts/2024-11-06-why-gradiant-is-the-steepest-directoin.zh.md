---
layout: page
title:  "为什么梯度是变化最快的方向？"
subtitle: 
date:   2024-11-06 10:21:21 +0530
categories: ["Analysis"]
lang: "zh"
---

在多元微积分、机器学习、优化和许多其他领域中，我们经常听到函数的**梯度方向**指向上升最快的方向。但为什么这是正确的呢？在这篇文章中，我们将深入探讨这一概念背后的原因，并了解梯度为何如此特殊。

梯度不仅在数学中扮演着重要角色，也在诸如通过梯度下降法训练机器学习模型、优化工程系统，甚至在经济学中确定最大利润点等实际应用中起着重要作用。梯度的概念对于解决我们需要找到最有效路径或解决方案的现实问题至关重要。如果你对这个概念有疑问或者需要复习一下，你来对地方了。

### 引言

当我们处理多个变量的函数（例如 $f(x, y)$）时，我们希望了解函数在任意点如何变化。梯度是实现这一目标的强大工具。梯度被定义为包含函数偏导数的向量，并指向函数值最陡增加的方向。

简单来说，想象一下你站在一座山上，想要找到爬山最快的方向。梯度向量所指的方向就是那个方向。

### 证明：梯度是函数变化最快的方向
<img src="{{ "/assets/img/blog_24_11_06_1.jpg" | relative_url }}" alt="描述图片的替代文本" style="width: 500px;height: auto;">
考虑一个**可微函数**（这是关键！否则，我们无法通过平面在局部近似函数） $ z = f(x, y) $ 在点 $ A(x_0, y_0) $ 处。我们可以用一个平面来局部近似这个函数：

<p style="text-align: center;">
$
    z' = ax + by + c.
$
</p>

$ z $ 的增量，用 $ \Delta z $ 表示，可以写为：

<p style="text-align: center;">
$
    \Delta z = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0).(1)
$
</p>

利用线性近似，也就是上图中的红色平面来近似这个目标函数：

<p style="text-align: center;">
$
    \Delta z' = a (x_0+\Delta x) + b(y_0+ \Delta y) + c - (ax_0 + by_0 + c) = a \Delta x + b \Delta y,
$
</p>

<p style="text-align: center;">
$
    \Delta z' = a \Delta x + b \Delta y. (2)
$
</p>

其中 $ a, b $ 是待定常数。$ \Delta z $ 和线性近似之间的误差，即上图中的黄色虚线：

$
    \Delta z - \Delta z' = \text{error}.
$

当 $ \Delta x, \Delta y \to 0 $ 时，我们将误差项表示为 $ \epsilon(\Delta x, \Delta y) $

由于函数是**可微的**，无论从哪个方向逼近，都可以保证误差项足够小。所以我们可以写为：

<p style="text-align: center;">
$\Delta z = a \Delta x + b \Delta y + \epsilon(\Delta x, \Delta y) \quad (3)$
</p>

此外，可微性意味着误差项为距离的高阶无穷小 $ o(\sqrt{(\Delta x)^2 + (\Delta y)^2}) $，即 $ \frac{\epsilon(\Delta x, \Delta y)}{\sqrt{(\Delta x)^2 + (\Delta y)^2}} \to 0$，其中 $ \sqrt{(\Delta x)^2 + (\Delta y)^2} $ 表示点 $ A(x_0, y_0) $ 和点 $ (x_0 + \Delta x, y_0 + \Delta y) $（图中的蓝线）的距离。

### 求 $ a $ 和 $ b $
我们首先设 $ \Delta y = 0 $，只考虑 $ x $ 方向的变化，可以得到 $ \Delta z $ 的两种表示方式，分别是**(1)**和**(3)**：

<p style="text-align: center;">
   $ \left. \frac{\Delta z}{\Delta x} \right|_{\Delta y = 0} =  \left.  \frac{(1)}{\Delta x} \right|_{\Delta y = 0}
    =\left. \frac{(2)}{\Delta x} \right|_{\Delta y = 0}$
</p>
<p style="text-align: center;">
$
    = \frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x} = \frac{a \Delta x + \epsilon(\Delta x, 0)}{\Delta x}.
$
</p>

Suprise！让 $ \Delta x \to 0 $，方程的左侧变为：

<p style="text-align: center;">
$
    \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x} = \frac{\partial f}{\partial x},
$
</p>

这正是函数 $ f $ 在点 $ A(x_0, y_0) $ 处关于 $ x $ 的**偏导数**定义，因此可以解出：

<p style="text-align: center;">
$
    a = \frac{\partial f}{\partial x},
$
</p>

同理对于 $ b $：

$
    b = \frac{\partial f}{\partial y}.
$

现在我们可以将线性近似重写为：

<p style="text-align: center;">
$
    \Delta z = \frac{\partial f}{\partial x} \Delta x + \frac{\partial f}{\partial y} \Delta y + \epsilon(\Delta x, \Delta y).
$
</p>

### 方向导数和变化最快的方向
最后我们可以开始讨论如何找到**变化最快的方向**。假设我们想找到函数 $ f(x, y) $ 在**单位向量** $ \mathbf{v} = (v_x, v_y) $ 方向上的变化率。我们从点 $ (x_0, y_0) $ 出发，沿向量 $ \mathbf{v} = (v_x, v_y) $ 的方向移动。

函数 $ f(x, y) $ 在方向 $ \mathbf{v} $ 上的变化率称为**方向导数**。方向导数定义为：

<p style="text-align: center;">
$
    \nabla_{\mathbf{v}} f(x, y) = \lim_{t \to 0} \frac{f(x_0 + t v_x, y_0 + t v_y) - f(x_0, y_0)}{t}.
$
</p>

因为 $ \mathbf{v} $ 是给定方向，沿着方向 $ \mathbf{v} $ 的轨迹可以表示为：

$
    \Delta x = t v_x, \quad \Delta y = t v_y.
$

我们可以将上述方程改写为：

<p style="text-align: center;">
$
    \nabla_{\mathbf{v}} f(x, y) = \lim_{t \to 0} \frac{f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0)}{t}= \lim_{t \to 0} \frac{\Delta z}{t}.
$
</p>

根据**(3)**，我们可以改写上述方程为：

<p style="text-align: center;">
$
    \nabla_{\mathbf{v}} f(x, y) = \lim_{t \to 0} \frac{a t v_x + b t v_y + \epsilon(t v_x, t v_y)}{t}.
$
</p>

当 $ t \to 0 $ 时，取极限得到：

$
    \nabla_{\mathbf{v}} f(x, y) = \frac{\partial f}{\partial x} v_x + \frac{\partial f}{\partial y} v_y.
$

### 结论
当**方向向量** $ \mathbf{v} = (v_x, v_y) $ 与**梯度向量**
$
    \nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)
$
一致时，方向导数达到最大值：

<p style="text-align: center;">
$ \nabla_{\mathbf{v}} f(x, y)=\frac{\partial f}{\partial x} v_x + \frac{\partial f}{\partial y} v_y = \text{dot}(\nabla f, \mathbf{v}) = \left| \nabla f \right| \left| \mathbf{v} \right| \cos \theta  $, 
</p>

其中 $ \theta $ 是 $ \nabla f $ 和 $ \mathbf{v} $ 之间的夹角。换句话说，**梯度**指向函数最陡增大的方向。

因此，当你站在山上并选择 $ \theta = 0^{\circ} $ 的方向时，你将以最快的速度上山。而当 $ v = (-\frac{\partial f}{\partial x}, -\frac{\partial f}{\partial y}) $，$ \theta = 180^{\circ} $ 时，你将以最快的速度下山，这也是为什么在机器学习中，或者在我们希望**最小化函数**的任务中，我们使用负梯度来在优化过程中更新权重。

#### 关于**梯度**与**梯度方向**
<img src="{{ "/assets/img/blog_24_11_06_2.jpg" | relative_url }}" alt="描述图片的替代文本" style="width: 800px;height: auto;">

刚开始接触梯度下降的时候一个让我感到迷惑的点在于，如果一个**方向**的梯度是负的，那么这个**方向**的反方向目标函数岂不是应该上升？哪来的梯度下降呢？

其实这里就是因为混淆了**梯度**和**梯度方向**。以上图一维为例，梯度退化为导数，当我们说梯度的时候，根据定义，是沿着数轴方向，*f(x)*的变化率，所以梯度反应了函数的变化率，而**梯度方向**则是将梯度应用回变量空间，指向函数增加最快的方向。

我们称句子中的第一个**方向**为**方向(1)**，第二个**方向**为**方向(2)**，第一句话的误区在于混淆了**方向(1)**与**方向(2)**，这里的**方向（1）**指的是沿着数轴方向，而**方向（2）**指的应该是**梯度方向**，所以如果**方向（1）**的梯度是负的，那么**方向（2）**应该是是指向了数轴的反方向，所以**方向（2）**的反方向恰恰是数轴方向，也就是目标函数下降的方向。

### Key Takeaways
- 如果函数是**可微的**，可以通过平面局部近似函数，得到 $ \Delta z = a \Delta x + b \Delta y + \epsilon(\Delta x, \Delta y) $。
- 并且 $a = \frac{\partial f}{\partial x}, b = \frac{\partial f}{\partial y}$。
- 我们使用**方向导数**来确定函数在给定方向上的变化率，并利用 $ \Delta z $ 的近似来找到**梯度向量**（函数的偏导数），**方向单位向量**和**方向导数**（函数在给定方向的变化率）之间的关系
  $ \nabla_{\mathbf{v}} f(x, y) = \frac{\partial f}{\partial x} v_x + \frac{\partial f}{\partial y} v_y $。
- 最后，我们发现当**方向单位向量**与**梯度向量**一致时，函数的**变化率**达到最大值，即**梯度向量**指向函数变化最快的方向。
