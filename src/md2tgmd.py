import re

def find_all_index(str, pattern):
    index_list = [0]
    for match in re.finditer(pattern, str, re.MULTILINE):
        if match.group(1) != None:
            start = match.start(1)
            end = match.end(1)
            index_list += [start, end]
    index_list.append(len(str))
    return index_list

def replace_all(text, pattern, function):
    poslist = [0]
    strlist = []
    originstr = []
    poslist = find_all_index(text, pattern)
    for i in range(1, len(poslist[:-1]), 2):
        start, end = poslist[i:i+2]
        strlist.append(function(text[start:end]))
    for i in range(0, len(poslist), 2):
        j, k = poslist[i:i+2]
        originstr.append(text[j:k])
    if len(strlist) < len(originstr):
        strlist.append('')
    else:
        originstr.append('')
    new_list = [item for pair in zip(originstr, strlist) for item in pair]
    return ''.join(new_list)

def escapeshape(text):
    return '▎*' + " ".join(text.split()[1:]) + '*\n\n'

def escapeminus(text):
    return '\\' + text

def escapeminus2(text):
    return r'@+>@'

def escapebackquote(text):
    return r'\`\`'

def escapebackquoteincode(text):
    return r'@->@'

def escapeplus(text):
    return '\\' + text

def escape_all_backquote(text):
    return '\\' + text

def dedent_space(text):
    import textwrap
    return "\n\n" + textwrap.dedent(text).strip() + "\n\n"

def find_lines_with_char(s, char, min_count):
    """
    返回字符串中每行包含特定字符至少min_count次的行的索引列表。

    参数:
    s (str): 要处理的字符串。
    char (str): 要计数的字符。
    min_count (int): 最小出现次数。

    返回:
    list: 满足条件的行的索引列表。
    """
    lines = s.split('\n')  # 按行拆分字符串

    for index, line in enumerate(lines):
        if re.sub(r"```", '', line).count(char) % 2 != 0 or (not line.strip().startswith("```") and line.count(char) % 2 != 0):
            # lines[index] = re.sub(r"`", '\`', line)
            lines[index] = replace_all(lines[index], r"\\`|(`)", escape_all_backquote)

    return "\n".join(lines)

def escape(text, flag=0):
    # In all other places characters
    # _ * [ ] ( ) ~ ` > # + - = | { } . !
    # must be escaped with the preceding character '\'.
    text = re.sub(r"\\\[", '@->@', text)
    text = re.sub(r"\\\]", '@<-@', text)
    text = re.sub(r"\\\(", '@-->@', text)
    text = re.sub(r"\\\)", '@<--@', text)
    if flag:
        text = re.sub(r"\\\\", '@@@', text)
    text = re.sub(r"\\`", '@<@', text)
    text = re.sub(r"\\", r"\\\\", text)
    if flag:
        text = re.sub(r"\@{3}", r"\\\\", text)
    text = re.sub(r"_", '\_', text)
    text = re.sub(r"\*{2}(.*?)\*{2}", '@@@\\1@@@', text)
    text = re.sub(r"\n{1,2}\*\s", '\n\n• ', text)
    text = re.sub(r"\*", '\*', text)
    text = re.sub(r"\@{3}(.*?)\@{3}", '*\\1*', text)
    text = re.sub(r"\!?\[(.*?)\]\((.*?)\)", '@@@\\1@@@^^^\\2^^^', text)
    text = re.sub(r"\[", '\[', text)
    text = re.sub(r"\]", '\]', text)
    text = re.sub(r"\(", '\(', text)
    text = re.sub(r"\)", '\)', text)
    text = re.sub(r"\@\-\>\@", '\[', text)
    text = re.sub(r"\@\<\-\@", '\]', text)
    text = re.sub(r"\@\-\-\>\@", '\(', text)
    text = re.sub(r"\@\<\-\-\@", '\)', text)
    text = re.sub(r"\@{3}(.*?)\@{3}\^{3}(.*?)\^{3}", '[\\1](\\2)', text)
    text = re.sub(r"~", '\~', text)
    text = re.sub(r">", '\>', text)
    text = replace_all(text, r"(^#+\s.+?\n+)|```[\D\d\s]+?```", escapeshape)
    text = re.sub(r"#", '\#', text)
    text = replace_all(text, r"(\+)|\n[\s]*-\s|```[\D\d\s]+?```|`[\D\d\s]*?`", escapeplus)
    text = re.sub(r"\n{1,2}(\s*\d{1,2}\.\s)", '\n\n\\1', text)
    # # 把 code block 以外的 - 替换掉
    text = replace_all(text, r"```[\D\d\s]+?```|(-)", escapeminus2)
    text = re.sub(r"-", '@<+@', text)
    text = re.sub(r"\@\+\>\@", '-', text)

    text = re.sub(r"\n{1,2}(\s*)-\s", '\n\n\\1• ', text)
    text = re.sub(r"\@\<\+\@", '\-', text)
    text = replace_all(text, r"(-)|\n[\s]*-\s|```[\D\d\s]+?```|`[\D\d\s]*?`", escapeminus)
    text = re.sub(r"```([\D\d\s]+?)```", '@@@\\1@@@', text)
    # 把 code block 里面的`替换掉
    text = replace_all(text, r"\@\@\@[\s\d\D]+?\@\@\@|(`)", escapebackquoteincode)
    text = re.sub(r"`", '\`', text)
    text = re.sub(r"\@\<\@", '\`', text)
    text = re.sub(r"\@\-\>\@", '`', text)

    # text = replace_all(text, r"`.*?`{1,2}|(`)", escapebackquoteincode)
    # text = re.sub(r"`", '\`', text)
    # text = re.sub(r"\@\-\>\@", '`', text)
    # print(text)

    text = replace_all(text, r"(``)", escapebackquote)
    text = re.sub(r"\@{3}([\D\d\s]+?)\@{3}", '```\\1```', text)
    text = re.sub(r"=", '\=', text)
    text = re.sub(r"\|", '\|', text)
    text = re.sub(r"{", '\{', text)
    text = re.sub(r"}", '\}', text)
    text = re.sub(r"\.", '\.', text)
    text = re.sub(r"!", '\!', text)
    text = find_lines_with_char(text, '`', 5)
    text = replace_all(text, r"(\n+\x20*```[\D\d\s]+?```\n+)", dedent_space)
    return text

text = r'''
# title

### `probs.scatter_(1, ind`

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

1. item 1
```python

# comment
print("1.1\n")_
\subsubsection{1.1}
- item 1 -
```
2. item 2

sudo apt install mesa-utils # 安装

\subsubsection{1.1}

And simple text `with-ten`  `with+ten` + some - **symbols**. # `with-ten`里面的`-`不会被转义


    ```
    print("Hello, World!") -
    app.listen(PORT, () => {
        console.log(`Server is running on http://localhost:${PORT}`);
    });
    ```

Cxy = abs (Pxy)**2/ (Pxx*Pyy)

`a`a-b-c`n`
\[ E[X^4] = \int_{-\infty}^{\infty} x^4 f(x) dx \]

`-a----++++`++a-b-c`-n-`
`[^``]*`a``b-c``d``
# pattern = r"`[^`]*`-([^`-]*)"``
w`-a----`ccccc`-n-`bbbb``a

1. 打开 VSCode 的终端：选择菜单中的 `视图` > `终端`，或者使用快捷键 `Ctrl+``（反引号）。

python line.strip().startwith("```")怎么写？

`视图` > `终端`

（\`）
- `Path.open()` 方法打开了 `README.md` 文件，并指定了编码为 `"utf-8"`。
'''

if __name__ == '__main__':
    import os
    os.system('clear')
    text = escape(text)
    print(text)