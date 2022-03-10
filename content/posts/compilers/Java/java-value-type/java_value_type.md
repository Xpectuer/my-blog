---
title: "【碎碎念】读《Java有值类型吗？》有感"
date: 2022-02-13T04:20:03+00:00
# weight: 1
# aliases: ["/first"]
tags: ['programming languages']
author: "Noobi"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "Java真的全是引用！！！"
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

# cover:
#     image: 
#  # image path/url
#     alt: "cover"
#     caption: "
#  <text>
#   " # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
editPost:
    URL: "https://github.com/Xpectuer/my-blog/content"
    Text: "Suggest Changes" # edit text
    appendFilePath: true # to append file path to Edit link
---

<!--
 * @Author: XPectuer
 * @LastEditor: XPectuer
-->




## 观点：

通过实现“**值类型**”，实现inline优化，又不改变Java**全是引用类型**的**语义**。

## 论据

思想实验：

```java
int x = 1;    // x指向内存地址A，内容是整数1
int y = x;    // （记住这个y） y指向同样的内存地址A，内容是整数1
x = 2;        // x指向另一个内存地址B，内容是整数2。y仍然指向地址A，内容是1。
System.out.println(x);
System.out.println(y);

// out:
// 可以看到
// 2
// 1
```

1. 引用类型特有那些操作？

   - dereference；例如C中`*a`
   - struct的分量访问和修改；例如，C中的`a.foo = 1`

    而对于「基本类型」，以上操作均不能实现。

    **前者**由于Java不提供；**后者**由于「基本类型」不是复合类型，也就无法实现。

2. 引用`=` 的语义？

   - 将引用绑定给一个新的对象。    

3. 那么我们的「基本类型」能做什么事情？

   - 读取它的值
   - 修改它的值

   那么，实际上，值类型的实现和引用类型的实现本质上的结果**完全一致。**

由此得出结论，对于「基本类型」，值类型和引用类型**等价**。

## 对这篇文章的疑惑

语义上，我们难道不是按照值类型的语义来传递参数的吗？

难道按照引用传递，不属于引用类型的语义吗？

```java
public void test() throws Exception{
        int x = 2;        
        foo(x);           // 传递了值
        System.out.println(x);
    }

public static  void foo(int x) {
        x = 3;
}

// out:
// 可以看见传递了值
// 2 

```

### **参数传递的语义？**

值传递：将**值**拷贝一份绑定给**参数**。

引用传递：将地址拷贝一份绑定给**参数。**

**实际上无需大费周章再证明一遍。**

注意我阐述的，不是放进参数列表（如果这么表述容易产生思维误区），而是绑定给**参数。**

那么**参数**，可以看作是「论据」中的`y`，「论据」的一切论述足以解释这个问题。

## 思考题

有人指出，Java 的引用类型可以是 null，而原始类型不行，所以引用类型和值类型还是有区别的。但是其实这并不能否认本文指出的观点，你可以想想这是为什么吗？

可能的解答：

首先，这是一种边界条件：

- 引用类型：我们只要同意：`null`值对应指向`0x0`的**地址**。
- 值类型：Java对于**基本类型**有初始化**置零**操作。比如，`int` 类型的零值为`0` 。

于是可以发现，对于「基本类型」，两种语义的确重合。



{{< pic src="/posts/compilers/Java/java-value-type/images/java_value_type.png"  alt="为什么引用类型null等价于值类型0？" >}} 


## 总结

思考这种基本问题，**不能保证百分百有用**，却有一种「明辨是非」的快乐。

我的感悟：

1. 即使是简单问题，也可以有严谨的讨论。不失为一次警示大脑的机会。
2. 在寻求答案过程中，甚至还能发现被一些“不求甚解”的前人扭曲的解释。
3. 思想实验的方法，可以很好地带动直觉论证一些结论。

## REF

[Yin Wang - Java 有值类型吗？](http://www.yinwang.org/blog-cn/2016/06/08/java-value-type)
