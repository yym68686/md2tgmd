# md2tgmd

md2tgmd is a Markdown to [Telegram-specific-markdown](https://core.telegram.org/bots/api#formatting-options) converter.

## Install

```bash
pip install md2tgmd
```

## Usage

~~~python
from md2tgmd import escape

text = '''
# title

**bold**
```
# comment
print(qwer) # ferfe
ni1
```
# bn

# b

# Header
## Subheader

[1.0.0](http://version.com)
![1.0.0](http://version.com)

- item 1 -
    - item 1 -
    - item 1 -
* item 2 #
* item 3 ~

1. item 1
2. item 2

sudo apt install mesa-utils # 安装

```python

# comment
print("1.1\n")_
\subsubsection{1.1}
```
\subsubsection{1.1}

And simple text `with-ten`  `with+ten` + some - **symbols**. # `with-ten`里面的`-`不会被转义


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

print(escape(text))


'''
▎*title*

*bold*
```
\# comment
print\(qwer\) \# ferfe
ni1
```
▎*bn*

▎*b*

▎*Header*
▎*Subheader*

[1\.0\.0](http://version\.com)
[1\.0\.0](http://version\.com)


• item 1 \-

    • item 1 \-

    • item 1 \-

• item 2 \#

• item 3 \~


1\. item 1

2\. item 2

sudo apt install mesa\-utils \# 安装

```python

\# comment
print\("1\.1\\n"\)\_
\\subsubsection\{1\.1\}
```
\\subsubsection\{1\.1\}

And simple text `with-ten`  `with+ten` \+ some \- *symbols*\. \# `with-ten`里面的`-`不会被转义


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

## Reference

https://github.com/skoropadas/telegramify-markdown


## License

This project is licensed under GPLv3, which means you are free to copy, distribute, and modify the software, as long as all modifications and derivative works are also released under the same license.