import re

def escapeshape(text):
    poslist = [0]
    strlist = []
    originstr = []
    regex = r"(#+\s.+?$)|```[\D\d\s]+?```"
    matches = re.finditer(regex, text, re.MULTILINE)
    for match in matches:
        start = match.start(1)
        end = match.end(1)
        if match.group(1) != None:
            poslist += [start, end]
            strlist.append('*' + text[start:end].split()[1] + '*')
    poslist.append(len(text))
    for i in range(0, len(poslist), 2):
        j, k = poslist[i:i+2]
        originstr.append(text[j:k])
    if len(strlist) < len(originstr):
        strlist.append('')
    else:
        originstr.append('')
    new_list = [item for pair in zip(originstr, strlist) for item in pair]
    # print(''.join(new_list))
    return ''.join(new_list)

def escape(text):
    # In all other places characters
    # _ * [ ] ( ) ~ ` > # + - = | { } . !
    # must be escaped with the preceding character '\'.
    text = re.sub(r"_", '\_', text)
    text = re.sub(r"\n\*", '\n• ', text)
    text = re.sub(r"\*", '\*', text)
    # text = re.sub(r"\[", '\[', text)
    # text = re.sub(r"\]", '\]', text)
    # text = re.sub(r"\(", '\(', text)
    # text = re.sub(r"\)", '\)', text)
    text = re.sub(r"~", '\~', text)
    text = re.sub(r"\.", '\.', text)
    text = escapeshape(text)
    text = re.sub(r"#", '\#', text)
    text = re.sub(r"\+", '\+', text)
    text = re.sub(r"\n-", '\n• ', text)
    text = re.sub(r"\-", '\-', text)
    text = re.sub(r"!", '\!', text)
    return text

text = '''
# 标题

```
# 注释
print(qwer) # ferfe
ni1
```
# bn

# b

# Header
## Subheader

[1.0.0](http://version.com)

- item 1 -
* item 2
* item 3 ~

```python
print("1.1")_
```

And simple text with + some - symbols.

当然可以！以下是Python的经典“Hello, World!”程序：

```
print("Hello, World!")
```

你可以将这段代码复制并粘贴到Python解释器中，或者将其保存到一个.py文件中并在命令行中运行它。无论哪种方式，它都应该输出“Hello, World!”这个简单的欢迎消息。
'''

message = (
    "我是人见人爱的 ChatGPT~\n\n"
    "欢迎访问 https://github.com/yym68686/ChatGPT-Telegram-Bot 查看源码\n\n"
    "有 bug 可以联系 @yym68686"
)
if __name__ == '__main__':
    text = escape(text)
    print(text)