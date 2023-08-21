# [RandomIntegerOutputer](https://github.com/Coriginbe/RandomIntegerOutputer/)

### 随机整数输出器
一个使用 Python 开发的 ~~简陋的~~ 简单的图形化界面随机整数输出程序（目前仅支持自然数）。  
A simple GUI random-integer-output-program developed in Python (Only Natural Numbers are currently supported).

---

### [Releases](https://github.com/Coriginbe/RandomIntegerOutputer/releases)

- **[随机整数打印器 V1.0](https://github.com/Coriginbe/RandomIntegerOutputer/releases/download/V1.0/RandomIntegerOutputer_V1.0_zh-Hans-CN.exe)**  

  2021/10/30

- **[随机整数输出器 V1.1](https://github.com/Coriginbe/RandomIntegerOutputer/releases/download/V1.1/RandomIntegerOutputer_V1.1_zh-Hans-CN.exe)**  

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
