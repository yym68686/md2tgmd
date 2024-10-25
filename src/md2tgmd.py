import re
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from latex2unicode import LaTeX2Unicode
l2u = LaTeX2Unicode()

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

def split_code(text):
    split_list = []
    if len(text) > 2300:
        split_str_list = text.split('\n\n')

        conversation_len = len(split_str_list)
        message_index = 1
        while message_index < conversation_len:
            if split_str_list[message_index].startswith('    '):
                split_str_list[message_index - 1] += "\n\n" + split_str_list[message_index]
                split_str_list.pop(message_index)
                conversation_len = conversation_len - 1
            else:
                message_index = message_index + 1

        split_index = 0
        for index, _ in enumerate(split_str_list):
            if len("".join(split_str_list[:index])) < len(text) // 2:
                split_index += 1
                continue
            else:
                break
        str1 = '\n\n'.join(split_str_list[:split_index])
        if not str1.strip().endswith("```"):
            str1 = str1 + "\n```"
        split_list.append(str1)
        code_type = text.split('\n')[0]
        str2 = '\n\n'.join(split_str_list[split_index:])
        str2 = code_type + "\n" + str2
        if not str2.strip().endswith("```"):
            str2 = str2 + "\n```"
        split_list.append(str2)
    else:
        split_list.append(text)

    if len(split_list) > 1:
        split_list = "\n@|@|@|@\n\n".join(split_list)
    else:
        split_list = split_list[0]
    return split_list

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

def latex2unicode(text):
    text = re.sub(r"\\\[", "", text)
    text = re.sub(r"\\\]", "", text)
    text = re.sub(r"\\\(", "", text)
    text = re.sub(r"\\\)", "", text)
    result = l2u.convert(text)
    # result = l2u.convert(rf"{text}")
    return result

def escape(text, flag=0, italic=True):
    # In all other places characters
    # _ * [ ] ( ) ~ ` > # + - = | { } . !
    # must be escaped with the preceding character '\'.
    text = replace_all(text, r"(\\\(.*?\\\))", latex2unicode)
    text = replace_all(text, r"(\\\[.*?\\\])", latex2unicode)
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
    # _italic_
    if italic:
        text = re.sub(r"\_{1}(.*?)\_{1}", '@@@\\1@@@', text)
        text = re.sub(r"_", '\_', text)
        text = re.sub(r"\@{3}(.*?)\@{3}", '_\\1_', text)
    else:
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

    # ~strikethrough~
    text = re.sub(r"\~{2}(.*?)\~{2}", '@@@\\1@@@', text)
    text = re.sub(r"~", '\~', text)
    text = re.sub(r"\@{3}(.*?)\@{3}", '~\\1~', text)

    # text = re.sub(r"\n>\s", '\n@*@ ', text, count=1)
    # matches = list(re.finditer(r"\n>\s", text))
    # if len(matches) >= 6:
    #     # 获取第五个匹配项的位置
    #     fifth_match = matches[5]
    #     start, end = fifth_match.span()

    #     # 只替换第五个匹配项
    #     text = text[:start] + '\n@*@ ' + text[end:]

    #     # 获取最后一个匹配项的位置
    #     last_match = matches[-1]
    #     start, end = last_match.span()

    #     # 找到该行的结束位置
    #     line_end = text.find('\n', end)
    #     if line_end == -1:  # 如果是最后一行
    #         line_end = len(text)

    #     # 在该行末尾添加 "||"
    #     text = text[:line_end] + '@!@' + text[line_end:]

    text = re.sub(r"\n>\s", '\n@@@ ', text)
    # print(text)
    text = re.sub(r">", '\>', text)
    # text = re.sub(r"\@\*\@", '**>', text)
    text = re.sub(r"\@{3}", '>', text)

    text = replace_all(text, r"(^#+\s.+?\n+)|```[\D\d\s]+?```", escapeshape)
    text = re.sub(r"#", '\#', text)
    text = replace_all(text, r"(\+)|\n[\s]*-\s|```[\D\d\s]+?```|`[\D\d\s]*?`", escapeplus)

    # 数字序号
    text = re.sub(r"\n{1,2}(\s*\d{1,2}\.\s)", '\n\n\\1', text)

    # 把 code block 以外的 - 替换掉
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
    text = re.sub(r"\s`\\`\s", ' `\\\\\` ', text)

    # text = replace_all(text, r"`.*?`{1,2}|(`)", escapebackquoteincode)
    # text = re.sub(r"`", '\`', text)
    # text = re.sub(r"\@\-\>\@", '`', text)
    # print(text)

    text = replace_all(text, r"(``)", escapebackquote)
    text = re.sub(r"\@{3}([\D\d\s]+?)\@{3}", '```\\1```', text)
    text = re.sub(r"=", '\=', text)
    text = re.sub(r"\|", '\|', text)
    # text = re.sub(r"\@\!\@", '||', text)
    text = re.sub(r"{", '\{', text)
    text = re.sub(r"}", '\}', text)
    text = re.sub(r"\.", '\.', text)
    text = re.sub(r"!", '\!', text)
    text = find_lines_with_char(text, '`', 5)
    text = replace_all(text, r"(\n+\x20*```[\D\d\s]+?```\n+)", dedent_space)
    # print(text)
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

为了匹配实际的点号，需要使用反斜杠 `\` 进行转义。

3. `(`

根据欧拉函数的性质，对于 \( n = p_1^{k_1} \times p_2^{k_2} \times \cdots \times p_r^{k_r} \)（其中 \( p_1, p_2, \ldots, p_r \) 是互不相同的质数），有：

\[ \varphi(n) = n \left(1 - \frac{1}{p_1}\right) \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_r}\right) \]

所以：

\[ \varphi(35) = 35 \left(1 - \frac{1}{5}\right) \left(1 - \frac{1}{7}\right) \]

计算每一步：

\[ \varphi(35) = 35 \left(\frac{4}{5}\right) \left(\frac{6}{7}\right) \]

\[ \varphi(35) = 35 \times \frac{24}{35} \]

\[ \varphi(35) = 24 \]

要计算加速度 \( a \)，我们可以使用以下公式：

\[ a = \frac{\Delta v}{\Delta t} \]

其中：
- \(\Delta v\) 是速度的变化量
- \(\Delta t\) 是时间的变化量

已知：
- 初速度 \( v_0 = 0 \) m/s
- 末速度 \( v = 27.8 \) m/s
- 时间 \( \Delta t = 3.85 \) s

我们可以将这些值代入公式：

\[ a = \frac{27.8 \, \text{m/s} - 0 \, \text{m/s}}{3.85 \, \text{s}} \]

计算得到：

\[ a = \frac{27.8}{3.85} \approx 7.22 \, \text{m/s}^2 \]

因此，这辆车的加速度约为 7.22 m/s²。

因此，欧拉函数 \( \varphi(35) \) 的值是 24。

'''

if __name__ == '__main__':
    import os
    os.system('clear')
    text = escape(text)
    print(text)

#     tmpresult = '''
# `🤖️ gpt-4o`

# To display the error message on the same page without redirecting, we can modify the form submission to use AJAX (Asynchronous JavaScript and XML) with `fetch`. This way, we can handle the response directly on the client side and update the DOM accordingly.

# ### Backend (TypeScript with Express.js)
# Ensure your backend route handles the login logic and returns JSON responses for errors and success:

# ```typescript
# import { Request, Response } from 'express';

# export async function workerLogin(req: Request, res: Response) {
#   try {
#       const { email, password } = req.body;
#       console.log(`Request Body: ${JSON.stringify(req.body)}`);

#       if (!email || !password) {
#           return res.status(400).json({ message: 'Email and password must be provided' });
#       }

#       const officeWorker = await getOfficeWorkerByEmail(email);

#       console.log('Found office worker:', officeWorker);

#       if (officeWorker && officeWorker.password === password) {
#           const workingHours = await getWorkingHoursByWorkerId(officeWorker._id);
#           console.log('Working hours:', workingHours);

#           const clientIds = [...new Set(workingHours.map(entry => entry.client_id))];
#           console.log('Client IDs:', clientIds);

#           const clients = await getClients({ _id: { $in: clientIds } });
#           console.log('Clients:', clients);

#           res.status(200).json({ redirectUrl: '/pages/manageClients', officeWorker, clients, clientsCount: clients.length });
#       } else {
#           res.status(400).json({ msg: 'Invalid Email or password' });
#       }
#   } catch (error) {
#       console.error('Error during worker login process:', error);
#       const errorMessage = error instanceof Error ? error.message : 'Unknown error';
#       res.status(500).json({ error: errorMessage });
#   }
# }
# ```

# ### Frontend (HTML + JavaScript)
# Modify your HTML form to handle the submission with JavaScript:

# ```html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link rel="stylesheet" href="/static/css/workerLogin.css">
#     <title>Worker Login</title>
# </head>
# <body>
#     <div class="container">
#         <h1>נתיג</h1>
#         <h1>:התחברות כעובד משרד</h1>
#         <form id="workerLoginForm">
#             מייל
#             <input type="email" name="email" placeholder="email" required>
#             סיסמה
#             <input type="password" name="password" placeholder="password" required>
#             <button type="submit">התחברות</button>
#         </form>
#         <div id="error-message" style="color: red; display: none;"></div>
#     </div>

#     <script>
#         document.getElementById('workerLoginForm').addEventListener('submit', async function(event) {
#             event.preventDefault(); // Prevent the form from submitting the traditional way

#             const form = event.target;
#             const formData = new FormData(form);
#             const data = Object.fromEntries(formData.entries());

#             const response = await fetch('/workerLogin', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify(data)
#             });

#             const result = await response.json();

#             if (response.status === 400) {
#                 // Show error message on the same page
#                 const errorMessage = document.getElementById('error-message');
#                 errorMessage.style.display = 'block';
#                 errorMessage.textContent = result.msg;
#             } else if (response.status === 200) {
#                 // Handle successful login (e.g., redirect to another page)
#                 window.location.href = result.redirectUrl;
#             } else {
#                 // Handle other errors
#                 const errorMessage = document.getElementById('error-message');
#                 errorMessage.style.display = 'block';
#                 errorMessage.textContent = result.error || 'An unknown error occurred';
#             }
#         });
#     </script>
# </body>
# </html>
# ```

# ### Explanation:
# 1. **Backend:** The `workerLogin` function now returns JSON responses for both success and error cases. On successful login, it includes a `redirectUrl` in the response.
# 2. **Frontend:**
#    - The form submission is intercepted by JavaScript using `event.preventDefault()`.
#    - The form data is collected and sent to the server using `fetch`.
#    - If the response status is `400`, the error message is displayed in a `<div>` on the same page.
#    - If the response status is `200`, the user is redirected to the URL provided in the response.
#    - Other errors are also handled and displayed.

# This approach ensures that users receive immediate feedback on the same page without needing to reload or navigate away.
# '''
#     replace_text = replace_all(tmpresult, r"(```[\D\d\s]+?```)", split_code)
#     if replace_text.strip().endswith("```"):
#         replace_text = replace_text.strip()[:4]
#     split_messages_new = []
#     split_messages = replace_text.split("```")

#     for index, item in enumerate(split_messages):
#         if index % 2 == 1:
#             item = "```" + item
#             if index != len(split_messages) - 1:
#                 item = item + "```"
#             split_messages_new.append(item)
#         if index % 2 == 0:
#             item_split_new = []
#             item_split = item.split("\n\n")
#             for sub_index, sub_item in enumerate(item_split):
#                 if sub_index % 2 == 1:
#                     sub_item = "\n\n" + sub_item
#                     if sub_index != len(item_split) - 1:
#                         sub_item = sub_item + "\n\n"
#                     item_split_new.append(sub_item)
#                 if sub_index % 2 == 0:
#                     item_split_new.append(sub_item)
#             split_messages_new.extend(item_split_new)
#     split_index = 0
#     for index, _ in enumerate(split_messages_new):
#         if len("".join(split_messages_new[:index])) < 3500:
#             split_index += 1
#             continue
#         else:
#             break
#     send_split_message = ''.join(split_messages_new[:split_index])

#     tmp = ''.join(split_messages_new[split_index:])
#     if tmp.strip().endswith("```"):
#         result = tmp[:-4]
#         matches = re.findall(r"(```.*?\n)", send_split_message)
#         if not result.strip().startswith("```") and len(matches) >= 1:
#             result = matches[-1] + result
#     else:
#         result = tmp
#     print(send_split_message)
#     print("================================")
#     print(result)
#     print(matches)
