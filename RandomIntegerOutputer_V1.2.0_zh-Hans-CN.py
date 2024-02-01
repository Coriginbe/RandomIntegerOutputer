import random
import webbrowser
from tkinter import *  # 导入 tkinter 模块中的所有公共函数、变量和类
from tkinter import font
from tkinter import messagebox  # 从 tkinter 模块导入 messagebox
from tkinter.messagebox import *  # 从模块 tkinter 的子模块 messagebox 中导入所有函数


root = Tk()
root.title('随机整数输出器 Ver. 1.2.0')
root.geometry('540x540')


def callback():
    if askokcancel('askokcancel', '''在打开的浏览器页面中，点击绿色按钮 “New Issues” 新建问题
在 “Title” 处输入标题， “Write” 处描述问题
注意：请勿提交无用信息'''):
        webbrowser.open('https://github.com/Coriginbe/RandomIntegerOutputer/issues')

def check_font(font_name):
    if font_name in font.families():
        return font_name
    else:
        return "SimHei"

def judge():
    num1 = input1.get()
    num2 = input2.get()
    if num1.isdigit() and num2.isdigit():
        num1, num2 = int(num1), int(num2)
        if num1 <= num2:
            var.set(random.randint(num1, num2))
        else:
            showerror('showerror', '''ValueError: empty range for randrange()
值错误：空范围''')
    else:
        showerror('showerror', '''SyntaxError: invalid character
语法错误：无效字符''')

# 定义一个函数，当 Entry 对象失去焦点时调用此函数
def restore_entry(event, entry, default_text):
    """
    参数:
    event: 一个描述了发生了什么的事件对象。在这种情况下，它描述了 Entry 对象失去焦点的事件。
    entry: 需要恢复默认文本的 Entry 对象。
    default_text: 当 Entry 对象失去焦点时需要恢复的默认文本。
    """
    if entry.get() == '':  # 如果 Entry 对象的内容为空
        entry.insert(0, default_text)  # 在 Entry 对象的开始位置插入默认文本
        entry.config(fg = 'grey', justify = 'center')  # 将 Entry 对象的文本颜色设置为灰色，并将文本居中
    else:
        entry.config(fg = 'black')


font_judge = check_font("得意黑")


input1 = Entry(root, font = ('SimHei', 25))
input1.insert(0, '起始数')  # 在 Entry 对象的开始位置插入文本 '起始数'
input1.bind('<FocusIn>', lambda event: input1.delete(0, 'end') if input1.get() == '起始数' else None)  # 当输入框获得焦点时，如果输入框的内容为 '起始数'，则清空输入框
input1.bind('<FocusOut>', lambda event: restore_entry(event, input1, '起始数'))  # 当输入框失去焦点时，如果输入框的内容为空，则将其设置为 '起始数'
input1.config(fg = 'grey', justify = 'center')
input1.place(relx = 0.225, rely = 0.1, relwidth = 0.2, relheight = 0.1)

input2 = Entry(root, font = ('SimHei', 25))
input2.insert(0, '结束数')  # 在 Entry 对象的开始位置插入文本 '结束数'
input2.bind('<FocusIn>', lambda event: input2.delete(0, 'end') if input2.get() == '结束数' else None)  # 当输入框获得焦点时，如果输入框的内容为 '结束数'，则清空输入框
input2.bind('<FocusOut>', lambda event: restore_entry(event, input2, '结束数'))  # 当输入框失去焦点时，如果输入框的内容为空，则将其设置为 '结束数'
input2.config(fg = 'grey', justify = 'center')
input2.place(relx = 0.6, rely = 0.1, relwidth = 0.2, relheight = 0.1)

var = StringVar()
Entry(root, state = 'readonly', textvariable = var, font = ('SimHei', 70), justify = 'center').place(relx = 0.25, rely = 0.4, relwidth = 0.5, relheight = 0.2)
Button(root, text = '输出', font = (font_judge, 30), command = judge).place(relx = 0.4, rely = 0.6, relwidth = 0.2, relheight = 0.1)

Feedback = Button(root, text = 'Feedback', font = (font_judge, 20), command = callback)
Feedback.place(relx = 0.75, rely = 0.75, relwidth = 0.2, relheight = 0.1)


root.mainloop()