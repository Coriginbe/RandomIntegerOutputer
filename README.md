# [RandomIntegerOutputer](https://github.com/Coriginbe/RandomIntegerOutputer/)

### 随机整数输出器
一个使用 Python 开发的 ~~简陋的~~ 简单的图形化界面随机整数输出程序（目前仅支持自然数）。  
A simple GUI random-integer-output-program developed in Python (Only Natural Numbers are currently supported).

---

## [Releases](https://github.com/Coriginbe/RandomIntegerOutputer/releases)


### [随机整数打印器 Ver. 1.0.0](https://github.com/Coriginbe/RandomIntegerOutputer/releases/download/V1.0.0/RandomIntegerPrinter_V1.0.0_zh-Hans-CN.exe)  

#### Release 时间：2021/10/30  


### [随机整数输出器 Ver. 1.1.0](https://github.com/Coriginbe/RandomIntegerOutputer/releases/download/V1.1.0/RandomIntegerOutputer_V1.1.0_zh-Hans-CN.exe)  

#### 更新时间：2021/10/31

- **新增功能**  
    - 增加了输入错误处理：如果输入的**起始数**大于**结束数**，或输入**非数字**，程序会弹出一个`showinfo`信息框提示错误。

- **改进**  
    1. 更改了程序名为 “随机整数输出器” 。  
    2. 将 “打印” `Button`的`text`更改为 “输出” 。  

- **Bug 修复**  
    - 修复了用户输入**非数字**或**起始数大于结束数**时程序崩溃的问题。  


### [随机整数输出器 Ver. 1.2.0](https://github.com/Coriginbe/RandomIntegerOutputer/releases/download/V1.2.0/RandomIntegerOutputer_V1.2.0_zh-Hans-CN.zip)   

#### 更新时间：2024/2/1  

**注意：建议使用程序前先安装 “得意黑 Smiley-Sans” 字体文件。**  
**“得意黑 Smiley-Sans” 官方 GitHub repository：https://github.com/atelier-anchor/smiley-sans**

- **新增功能**
    - 增加了反馈功能：用户可以点击 “Feedback” `Button`，跳转到 GitHub repository 的 Issues 页中新建 Issues 。

- **改进**
  1. 调整了结束数`Entry`的位置。  
  2. 更改了`Entry`尺寸。  
     - 输入`Entry`的相对宽度`relwidth`由`0.1`改为`0.2`，相对高度`relheight`由`0.05`改为`0.1`  
     - 输出`Entry`的相对宽度`relwidth`由`0.2`改为`0.5`  
  3. 更改了文本字体`font(family)`。  
     - 输入和输出`Entry`内`font(family)`由`NSimSun`改为`SimHei`。  
     - `Button`内`font(family)`改为`得意黑`，如系统无安装`得意黑`字体则使用`SimHei`。   
  4. 更改了字体大小`font(size)`。  
     - 输入`Entry`内`font(size)`由`15`改为`25`  
     - 输出`Entry`内`font(size)`由`30`改为`70`  
     - 输出`Button`内`font(size)`由`15`改为`30`  
  5. `Entry`内文本居中。  
  7. 输出`Entry`的状态`state`设为只读`readonly`。  
  8. 修改了输入错误消息框：消息框由`showinfo`改为`showerror`，并增加错误信息的中文翻译。  

- **Bug 修复**
  - 优化了`judge`函数的逻辑。在比较输入的`num1`（起始数）和`num2`（结束数）之前，先将两个数转换为整数类型`int`，避免因字符串比较导致的错误结果。
