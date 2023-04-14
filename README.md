# md2tgmd

md2tgmd is a Markdown to [Telegram-specific-markdown](https://core.telegram.org/bots/api#formatting-options) converter.

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

- item 1 -
* item 2
* item 3 ~

```python
print("1.1")_
```

And simple text with + some - **symbols**.


```
print("Hello, World!")
```
'''

print(escape(text))


'''
▎*title*

*bold*
```
\# comment
print(qwer) \# ferfe
ni1
```
▎*bn*

▎*b*

▎*Header*
▎*Subheader*

[1\.0\.0](http://version\.com)

• item 1 \-
• item 2
• item 3 \~

```python
print("1\.1")\_
```

And simple text with \+ some \- *symbols*\.


```
print("Hello, World\!")
```

'''

~~~

## Reference

https://github.com/skoropadas/telegramify-markdown