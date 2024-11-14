# md2tgmd

[English](README.md) | [Chinese](README_CN.md)

md2tgmd is a Markdown to [Telegram-specific-markdown](https://core.telegram.org/bots/api#formatting-options) converter.

## Feature

- Supports most of the specific Markdown syntax for Telegram, including: headings, bold, italic, strikethrough, code blocks, links, and quotes.
- Support the conversion of LaTeX formulas in Markdown to Unicode characters to improve the readability of mathematical formulas in Telegram.
- Support syntax highlighting for code blocks in Markdown.

## Install

```bash
pip install md2tgmd
```

## Usage

~~~python
From md2tgmd import escape

text = '''
# Title

\[ \\varphi(35) = 35 \\left(1 - \\frac{1}{5}\\right) \\left(1 - \\frac{1}{7}\\right) \]

**Bold**
```
# Comment
print(qwer) # ferfe
ni1
```
# bn

# b

# Title
## Subtitle

[1.0.0](http://version.com)
![1.0.0](http://version.com)

- Item 1 -
    - Item 1 -
    - Item 1 -
* Item 2 #
* Item 3 ~

1. Item 1
2. Item 2

sudo apt install mesa-utils # Install

```python

# Comment
print("1.1\n")_
\subsubsection{1.1}
```
\subsubsection{1.1}

And simple text `with-ten`  `with+ten` + some - **symbols**. # `-` inside `with-ten` will not be escaped


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
▎*Title*

ϕ(35) = 35(1 - ⅕)(1 - 1/7)

*Bold*
```
\# Comment
print\(qwer\) \# ferfe
ni1
```
▎*bn*

▎*b*

▎*Title*
▎*Subtitle*

[1\.0\.0](http://version\.com)
[1\.0\.0](http://version\.com)


• Item 1 \-

    • Item 1 \-

    • Item 1 \-

• Item 2 \#

• Item 3 \~


1\. Item 1

2\. Item 2

sudo apt install mesa\-utils \# Install

```python

\# Comment
print\("1\.1\\n"\)\_
\\subsubsection\{1\.1\}
```
\\subsubsection\{1\.1\}

And simple text `with-ten`  `with+ten` \+ some \- *symbols*\. \# `-` inside `with-ten` will not be escaped


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