---
title: "GNU make tricks"
date: 2022-04-27T11:30:03+00:00
# weight: 1
# aliases: ["/first"]
#tags: []
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

# GNU make tricks

Author: Me
Type: System

在理解 [abstract machine](https://github.com/NJU-ProjectN/abstract-machine) 的过程中，难免需要理解Makefile做了什么。

于是有了：

```
make -nB
```

可以查看编译选项和编译过程，

但是可读性极差，而且无法直接导出到文件（原因待探索，推测由于输出不是从`stdout`出去的）。

```bash
make -nB ARCH=x86_64-qemu  \
        | grep -ve '^\(\#\|echo\|mkdir\|make\)' \
         | sed "s#$AM_HOME#\$AM_HOME#g" \
          | sed "s#$PWD#.#g" | vim -                         

# OSX不适用以上的脚本，因为OSX的 sed 对于path name escape的支持很差
```

注意：要`vim -` 才能让`vim`从`stdin`读数据

> `-`  The file to edit is read from stdin. Commands are read from stderr, which should be a tty.
                                                                                                                                   ——— man vim
> 

进去vim，我们又有一些小的trick帮助我们进行formatting

```bash
: set nowrap
: %s/ /\r\t/g 
```

美滋滋 😀

```bash
x86_64-linux-gnu-gcc
        -std=gnu11
        -O2
        -MMD
        -Wall
        -Werror
				- ...
...
```
