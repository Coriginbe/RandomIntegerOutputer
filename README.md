# RandomIntegerOutputer

### 随机整数输出器
一个 ~~简陋的~~ 简单的随机整数输出程序（目前仅支持自然数）。  
A ~~crude~~ simple random integer output program (Only natural numbers are currently supported).

---

### 更新日志
- **随机整数打印器 V1.0**

  2021/10/30

- **随机整数输出器 V1.1**  

  2021/10/31

  更换程序名称  
  修改 `root.title()`  
  ```
  root.title('随机整数输出器 V1.1')
  ```
  修改 `Button(text)`
  ```
  Button(root,text='输出',font=('NSimSun',15),command=judge).place(relx=0.4,rely=0.6,relheight=0.1,relwidth=0.2)
  ```

  从模块 `tkinter` 的子模块 `messagebox` 中导入所有函数  
  ```
  from tkinter.messagebox import *
  ```

  在 `judge()` 函数中增加 `range for randrange()` 判断和 `character` 判断并使用 `showinfo` 提示 `Error` 
  ```
    elif num1>num2:
        showinfo('Info','ValueError: empty range for randrange()')
    else:
        showinfo('Info','SyntaxError: invalid character')
  ```
