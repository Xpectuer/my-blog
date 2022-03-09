---
title: "Continuation"
date: 2022-03-08T11:30:03+00:00
# weight: 1
# aliases: ["/continuation"]
tags: ["programming language"]
author: "Noobi"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "Desc Text."
canonicalURL: "https://canonical.url/to/page"
disableHLJS: true # to disable highlightjs
disableShare: true
disableHLJS: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
mathjax: true

cover:
    image: "<image path/url>" # image path/url
    alt: "<alt text>" # alt text
    caption: "<text>" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: true # only hide on current single page
editPost:
    URL: "https://github.com/Xpectuer/my-blog/content"
    Text: "Suggest Changes" # edit text
    appendFilePath: true # to append file path to Edit link
---

# 续体 Continuation

> 英国作家叶芝说：“教育不是注满一桶水，而是点燃一把火。” 
>
> 但是你必须先“给桶注一点水“。
>
> -------《Operating System: Three Easy Pieces》

对于我这样一个PL门外汉来说，读王垠的博客可以用丰收（Harvest）来形容。

如同普罗米修斯为无知的人类带来智慧的火焰，引导人们向未知前进。

很多人说，难以理解Python的generator，难以理解Coroutine。

然而，在我们理解了续体后，一切都迎刃而解，generator不过就是Python团队空造出来的概念罢了；我们甚至可以利用这个概念，构造一个区别于Unix线程概念的操作系统（基于Coroutine的系统）。

### 什么是续体（Continuation）

任何的**过程**（procedure）都可以被抽象成一个**自动机**（Automata）。

过程的组成无非几点：

1. （输入）/输出
2. 一系列动作（$state_A \rightarrow state_B$） 
3. 一系列状态（$state_A,state_B,...,state_N$）

每个过程又被所谓的帧（Frame）包装，以便保存一些状态。

过程具有一个性质：**<u>一旦返回，内部的状态不留存。</u>**

例如，有如下C函数:

```java
int foo(int a) {
	int b = a + 1;
	return b;
}
```

当函数返回时，`b`的值被返回出来，但是`b`不复存在。

> 如同插座一样，插头插入电源，电流流出，但插座里面的铁片还在原地。

于是，过程调用者（Caller）的状态可以被一种LIFO的结构，即栈结构保存。



然而，如果人们的认知止步于此，如同人们如果只甘心将数域扩充到有理数，无穷之谜无从解答，解析几何将烟消云散，微积分将失去基石，于是现代物理无从发展...直到计算机也无法发展，阁下将没有机会看到这篇文章 ;(



回归正题，与**希帕索斯提出$\sqrt 2$ 一样**，有人提出疑问，为什么一个”过程“非得返回就退出了？

如果您玩过电子游戏，直觉会告诉我们，电子游戏暂停之后，怪物们似乎并没有消失或是停止攻击动作...



类比过程，我能否让一个”过程“执行了一半然后先返回？

于是，“续体”的概念被扩充了出来，它是“过程”的泛化（generalization）。



看下面这段python代码：

```python
def foo():
	i = 0	
	for j in range(5):
		yield i;
		i = i + 1		
```

如果我调用它一次，它只会返回一个值（我不打算解释generator，因为那不重要）。



由于Python generator的机制，我需要利用迭代的方式函数才能得到每个返回值。

```python
for i in foo():
	print(i)

# outputs:
0
1
2
3
4
```

实际上，每次循环的时候，都调用了一次`foo()` 。

然而，从输出明显可以看到，显然`foo()` **保留了上一次调用的状态**（不然`i`就不会加1了）。

这就是续体的概念，与函数很像，但是它在返回时依然保存自己的状态，如同被“冻结”了一般。



### 总结

总结一下，过程在返回时，内部的状态不再留存；

而为了更加通用的目的，人们将这个性质出发，扩充出了“续体（continuation）”的概念。

从定义角度出发，“续体”是“过程”的超集，即“过程”是特殊的“续体”（不需要保存状态）。









