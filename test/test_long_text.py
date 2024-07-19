
b = '''
```
fvewfv
```
nknknlnkj
```
kjbkjbk
'''
print(b.split('```'))
a = '''
'''

print(len(a))  # 1911

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.md2tgmd import replace_all, split_code
text = replace_all(a, r"(```[\D\d\s]+?```)", split_code)
print(text)
# for i in split_code(a):
#     print(i)