# Output-Random-Integer

### 输出随机整数
一个 ~~简陋的~~ 简单的输出随机整数（目前仅支持自然数）的图形化程序。  
A ~~crude~~ simple graphical program of outputting random integer ( Only supports Natural Number currently ) .

---

### 更新日志
- **打印随机整数 V1.0**

  2021/10/30

- **输出随机整数 V1.1**  

  2021/10/31

  更换程序名称  
  更新 `root.title`  
  `root.title('输出随机整数 V1.1')`

  从模块 tkinter 的子模块 messagebox 中导入所有函数  
  `from tkinter.messagebox import *`  

  在 `judge()` 函数中增加 `randrange()` 范围判断和 `invalid character` 判断并使用 `showinfo` 提示
  ```
    elif num1>num2:
        showinfo('Info','ValueError: empty range for randrange()')
    else:
        showinfo('Info','SyntaxError: invalid character')
  ```
