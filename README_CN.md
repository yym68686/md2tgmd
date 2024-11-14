# md2tgmd

[English](README.md) | [Chinese](README_CN.md)

md2tgmd 是一个将 Markdown 转换为 [Telegram 特定 Markdown](https://core.telegram.org/bots/api#formatting-options) 的转换器。

## 安装

```bash
pip install md2tgmd
```

## 用法

~~~python
从 md2tgmd 导入 escape

文本 = '''
# 标题

**加粗**
```
# 注释
print(qwer) # ferfe
ni1
```
# bn

# b

# 标题
## 子标题

[1.0.0](http://version.com)
![1.0.0](http://version.com)

- 项目 1 -
    - 项目 1 -
    - 项目 1 -
* 项目 2 #
* 项目 3 ~

1. 项目 1
2. 项目 2

sudo apt install mesa-utils # 安装

```python

# 注释
print("1.1\n")_
\subsubsection{1.1}
```
\subsubsection{1.1}

以及简单文本 `with-ten`  `with+ten` + 一些 - **符号**。 # `with-ten`里面的`-`不会被转义


```
print("Hello, World!") -
```

Cxy = abs (Pxy)**2/ (Pxx*Pyy)

`a`a-b-c`n`

`-a----++++`++a-b-c`-n-`
`[^``]*`a``b-c``d``
# pattern = r"`[^`]*`-([^`-]*)``
w`-a----`ccccc`-n-`bbbb``a
'''

print(escape(文本))


'''
▎*标题*

*加粗*
```
\# 注释
print\(qwer\) \# ferfe
ni1
```
▎*bn*

▎*b*

▎*标题*
▎*子标题*

[1\.0\.0](http://version\.com)
[1\.0\.0](http://version\.com)


• 项目 1 \-

    • 项目 1 \-

    • 项目 1 \-

• 项目 2 \#

• 项目 3 \~


1\. 项目 1

2\. 项目 2

sudo apt install mesa\-utils \# 安装

```python

\# 注释
print\("1\.1\\n"\)\_
\\subsubsection\{1\.1\}
```
\\subsubsection\{1\.1\}

以及简单文本 `with-ten`  `with+ten` \+ 一些 \- *符号*\. \# `with-ten`里面的`-`不会被转义


```
print\("Hello, World\!"\) -
```

Cxy \= abs \(Pxy\)\*\*2/ \(Pxx\*Pyy\)

`a`a\-b\-c`n`

`-a----++++`\+\+a\-b\-c`-n-`
`\[^\`\`\]\*`a\`\`b\-c\`\`d\`\`
▎*pattern*
w`-a----`ccccc`-n-`bbbb\`\`a
'''
~~~

## 参考文献

https://github.com/skoropadas/telegramify-markdown


## 许可证

本项目根据 GPLv3 许可，这意味着您可以自由复制、分发和修改软件，只要所有修改和衍生作品也根据相同的许可发布。