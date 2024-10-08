---
title: Lecture_03_Function
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css: assets/custom.css
revealOptions:
    transition: 'slide'
    transitionSpeed: fast
    center: false
    slideNumber: "c/t"
    width: 1000
---


<div style="display: flex; justify-content: center; align-items: center; height: 700px;">
  <div style="text-align: center; padding: 40px; background-color: white; border: 2px solid rgb(0, 63, 163); border-radius: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.1);">
    <h1 style="font-size: 48px; font-weight: bold; margin-bottom: 20px; color: #333;">SI100+ 2024 Python Lecture 3</h1>
    <p style="font-size: 24px; color: #666;">函数</p>
    <p style="font-size: 16px; color: #999; margin-top: 20px;">SI100+ 2024  Staff | 2024-08-26</p>
  </div>
</div>

<!--s-->

# 00. 在开始之前

<!--v-->

## 如何查询已有函数的用法

- 我们已经学会了调用 `print`, `input` 来完成一些基本操作
- 但是 Python 还有很多函数，即使是 `print`, `input` 也有很多用法
- 如何查询？

<!--v-->

## `help()`

**这是什么**

- `help()` 可以查看某函数或对象的帮助
- 在交互式命令行中
	- 输入 `help()` 并按下回车，可以进入交互式 `help` 环境（不太常用）
	- 输入 `help(x)` 并按下回车，可以看到关于 `x` 的帮助（`less` 模式）
		- 如果 `x` 是函数那么则是对于这个函数的帮助
		- 如果 `x` 是某个类型的字面值 / 变量，那么则是对于这个类型的帮助
- 在其他情况下，`help()` 就相当于 "`print(帮助内容)` "

<!--v-->

在交互式控制台（打开 Anaconda Prompt / Terminal，输入 Python 并回车后）

```py
>>> help(print)
Help on built-in function print in module builtins:
# 上面告诉了你 `print` 是一个内置函数，在模块 `builtins` 里（之后会讲）
print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
# 上面两行分别是 `print` 的用法（也就是定义）和作用描述
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
# 下面是在解释在用法出现的“参数”含义（还记得 end 吗？）
~
(END)
```

+ ***怎么退出啊啊啊啊啊啊！！！**

<!--v-->

## \[番外\] `less` ：只是为了看长长的报错

- Python 的控制台中的 `help` 使借用 `less` 命令输出的，在 `linux` 下，它是用来“展示”输出的（否则内容过多就会溢出屏幕而丢失）
- 在很久以前，计算机里只有 `vi` 编辑器，它规定的 `:q` 退出， `J/K` 用来上下翻页，`Ctrl+U/D` 快速上下翻页。而这成为了当时的习惯，被沿用下来。
- 当时 `less` 的作者 Mark Nudelman 只是想“方便的翻阅长长的报错”
	- 他当时用的 `vi` 版本不能打开这么大的日志文件
	- 另一个叫 `more` 的工具虽然能打开，但是不能向回翻<small>（现在似乎有了）</small>
- `less` = `vi` 的操作模式 + `more` 的文件支持 的“查看器” （文件分页器）

<div style="column-count: 2; padding-left: 20vh; padding-right: 20vh">

<img src="https://www.globalnerdy.com/wp-content/uploads/2012/04/geeks-and-repetitive-tasks.jpg" width=300/>

- 极客的浪漫莫过于此
- 编程：重复事情上制胜的法宝

</div>

<!--v-->

## 代码提示：VSCode 为什么比记事本好

- 将鼠标悬浮在 `print` 上，会弹出来一个小提示，会简单告诉你用法

```py
(function) # 告诉我们 `print` 是一个函数
def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None: ...
# 课后查阅资料：为什么会有两个 `print`？？？
def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: _SupportsWriteAndFlush[str] | None = None,
    flush: bool
) -> None: ...
```

<!--v-->

## 代码提示 (cont' d)

- 除了鼠标悬浮，在你一边输入 `print(...)` 的时候，代码提示也会出现
- 并且会用醒目的标识来指示你正在输入哪个参数

```py
# 尝试在 VSCode 中缓慢打出
print("Hello", end="!")
```

<!--v-->

## IPython 的小问号 `?`

- 在 Jupyter Notebook / IPython 里，我们可以直接用 `?` 接在函数名字的末尾

```py
In [1]: print?
Signature: print(*args, sep=' ', end='\n', file=None, flush=False)
# 上面告诉了我们用法格式/定义，下面这一串是 docstring (函数自身携带的文档的内容)
Docstring:
Prints the values to a stream, or to sys.stdout by default.

sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush
  whether to forcibly flush the stream.
# 最后告诉我们这是一个“内置函数或方法”
Type:      builtin_function_or_method
```

<!--v-->

## 内置函数(?)初探

- `len(str)`: `str` 的长度
- `max(a, b)`: `a` 与 `b` 中最大值
- `min(a, b)`: `a` 与 `b` 中最小值
- `abs(x)`: `x` 的绝对值
- `str.upper()` 全大写的 `str`
- `str.lower()` 全小写的 `str`
- `str.capitalize()` 首字母大写的 `str`
- `str.replace(str1, str2)` 将 `str` 中的所有 `str1` 替换成 `str2`
- `str.replace(str1, str2, N)` 同上，但最多只替换 `N` 次
- `str.isupper()` `str` 是否全是大写字母（布尔类型）
- `str.isdigit()` `str` 是否全是数字（布尔类型）
- `str.isalpha()` `str` 是否全是字母（布尔类型）
- `str.isalnum()` `str` 是否全是数字或字母（布尔类型）

<!--v-->

**演示** `"ABC123".isupper()"`

- <span>为什么是 `True`?</span> <!-- .element: class="fragment" data-fragment-index="1" -->
- <span>`help("ABC123".isupper)` 一下？</span> <!-- .element: class="fragment" data-fragment-index="2" -->

> 尽管我们用简短的文字介绍了他们，但是还有很多细节是我们忽略了的
> 
> 使用函数的时候切记不可以 **望文生义**，遇到行为奇怪的函数，应该查文档和它的 Docstring
<!-- .element: class="fragment" data-fragment-index="3" -->

<!--s-->

# 01. 函数与方法

<!--v-->

## 函数 (function)

- 为什么要有函数？
	- 数学中，“令 $f(x) = x^{2}+2x+1$” 可以让我们过程更简洁
	- 编程中，定义一个函数可以**防止重复的代码**（代码复用）
- 函数是什么？
	- 独立的代码块，通过名称调用
	- 通俗理解，函数就是大段代码的“替身”

<!--v-->

## 方法 (method)

- 什么是方法？我怎么从来没听说过？
	- 还记得我们之前的疑问吗？
	- 为什么有些“函数”是可以直接用的 (`print`)
	- 有些“函数”要用一个 `.` 连接才能使用？(`isdigit`)

**演示** 方法的“依赖性”

```py
print("123".isdigit())
print(123.isdigit())
```

<!--v-->

## 方法 (method) (cont'd)

- 方法区别于函数，它不是 **随处可用** 的，而是 **依赖** 某个特定的字面值/变量
	- 例如，上述例子中，只有 `str` 类型的字面值/变量才能够使用 `.isdigit()`
	- P.S. 在 `IPython` / `Notebook` 中，也必须用 `类型名.方法名?` 来获取帮助
		- 但可以直接 `help(变量/字面值.方法名)` 和悬浮
- 我们并不会在这次课程中涉及到怎么写 **方法**，因为还需要很多面向对象的前置知识，在 SI 100B 正课里面（也许会）涉及

<!--v-->

## Re: 内置函数和方法初探

- `len(str)`: `str` 的长度
- `max(a, b)`: `a` 与 `b` 中最大值
- `min(a, b)`: `a` 与 `b` 中最小值
- `abs(x)`: `x` 的绝对值
- `str.upper()` 全大写的 `str`
- `str.lower()` 全小写的 `str`
- `str.capitalize()` 首字母大写的 `str`
- `str.replace(str1, str2)` 将 `str` 中的所有 `str1` 替换成 `str2`
- `str.replace(str1, str2, N)` 同上，但最多只替换 `N` 次
- `str.isupper()` `str` 是否全是大写字母（布尔类型）
- `str.isdigit()` `str` 是否全是数字（布尔类型）
- `str.isalpha()` `str` 是否全是字母（布尔类型）
- `str.isalnum()` `str` 是否全是数字或字母（布尔类型）

<!--v-->

# 太酷了，还有更多吗

<!--v-->

## 引入库 (Import Packages)

- Python 自带了很多库，相当于有很多“工具箱”
- 我们可以使用 `import` 语句导入库，从而使用工具箱里的工具

```py
import math # 导入数学库

print(math.sqrt(16)) # 使用数学库里的平方根函数

import random # 导入随机数库

print(random.randint(1,100)) # 输出在 [a,b] 中的的随机整数
print(random.random()) # 输出在 0.0 <= x < 1.0 之间的随机小数
```

- 也有些强大的库需要额外安装，这些将会在之后涉及

<!--s-->

# 02. 定义函数、调用函数、返回值

<!--v-->

## 先尝试自己理解

下面是对 $f(x) = x^{2}+2x+1$ 的简单实现

```py []
def f(x):
	ans = x ** 2 + 2 * x + 1
	return ans
```

- 尝试运行
+ **无事发生。。。**

<!--v-->

## 先尝试自己理解 (cont'd)

哦哦哦！！单纯的写函数而不调用，就像单纯 令 $f(x)=...$ 而不计算一样  
**是没有效果的！**

下面是对 $f(x) = x^{2}+2x+1$ 的简单实现（附**调用**）

```py []
def f(x):
	ans = x ** 2 + 2 * x + 1
	return ans

print(f(2))
```


**Magic!**

<!--v-->

## `def` - 定义函数

```py [1]
def f(x):
	ans = x ** 2 + 2 * x + 1
	return ans
```

- 要定义一个函数，我们会用关键字 `def` 开头，后接函数名称和一对圆括号
- 圆括号里面的“变量”叫做**参数** (Parameter)，可以有多个，用逗号分隔
- 圆括号里写下的变量可以直接在函数里面使用，实际的值将由调用时 **真正的参数** 决定
	- 例如 `f(2)` 会自动将 `x` 赋值为 `2`，这样才计算得出了正确的结果
- **一定不要忘记那个冒号！**
	- 冒号相当于告诉 Python 我们的函数到底有“多长”
	- 具体多长那就是靠**缩进**解决，冒号后面跟的是有 4 个空格的代码，那下面紧挨着的所有 4 个空格开始的代码都是函数“内容”~
- **定义不一定会被执行**（目前理解为不会执行就好）

<!--v-->

**函数定义的格式**

```py []
def 函数名(参数, 参数, ...):
    函
    数
    体
```

**演示** 谁在内部

```py [0|5|6|1,2,3|2|3|1,2,3,6|7|0]
def fun(): # 定义一个不需要参数的函数，定义不会执行
	print("我在函数内部！")
	print("我也在函数内部！")

print("我不在函数内部！")
fun()
print("我当然也不在函数内部")
```

<!--v-->

那如果我们换一个顺序呢？

**演示** 函数调用顺序

```py []
g("初音未来")

def g(chara):
	print("我去,", chara, "!")
```

- 居然报错了？
  
```py
NameError                      Traceback (most recent call last)
Cell In[?], line 1
----> 1 g("初音未来")
      3 def g(chara):
      4 	print("我去,", chara, "!")

NameError: name 'g' is not defined
```

- 换回来呢 <span>好了</span> <!-- .element: class="fragment" data-fragment-index="1" -->

<!--v-->

## 为什么动漫里要先喊技能名

- 函数必须先声明才能调用
	- 什么是声明？就是从 `def` 一直到代码块结束！

> <img src="images/define.jpg" width="45%" style="display: block; margin: 0 auto;">

<!--v-->

## `return`：返回计算的结果

```py[3]
def f(x):
	ans = x ** 2 + 2 * x + 1
	return ans
```

- 函数存在的意义是什么？复用代码，从而更方便地
	- 执行某些代码
	- 计算某些值
- `return` 就是用来 **返回** 这个计算的值，倘若一个函数始终没有 `return` 执行完成后相当于返回了一个 `None` (代表什么都没有)
- 倘若计算完成，那使命也就完成了！也就没有继续运行的意义了！（函数终结者）

<!--v-->

## `return`：返回计算的结果 (cont'd)

**演示** 有返回值和无返回值

```py []
def calc1(x):
	ans = x ** 2

def calc2(x):
	ans = x ** 2
	return ans

def calc3(x):
	return x ** 2 # return 也可以直接返回

print(calc1(2), calc2(2), calc3(2))
```

<!--v-->

**演示** `return` 之后不会继续运行函数

```py [8|2|3|4|5|1-5,8]
def ChuanShanJia():
	print("Gui Ye 先生")
	print("Tian Huang 陛...下")
	print("我滴任务完成辣")
	return "拉开了手榴弹，并没有爆炸"
	print("啊哈哈哈哈哈哈哈哈") # 笑不出来

print(ChuanShanJia())
```

- `return` 可以提前结束函数，通常会在以后的以下情况遇到
	- 某些情况输入就是错的，执行函数没有意义或者会导致崩溃
	- 某些情况是特定的，需要返回特定的值
	- 某些情况是更简单地，可以用更简单的方法计算并返回
- 以上的 **某些情况** 都代表了一种“只有特定条件才会触发”的含义，我们会在下一节课（控制流）中学会它！

<!--s-->

# 03. 参数

<!--v-->

## 参数：函数沟通的桥梁

- 刚才的例子中我们探索了如何传递参数，现在我们来看看参数到底是什么
- 参数按照**出现位置**可以简单分为形式参数 (Parameter) 和实际参数 (Argument)
	- 形式参数：就是写在定义处的参数 `def f(x1, x2):...`
		- 除了会作为变量使用之外，还能规定函数的形式（长什么样）
	- 实际参数：就是调用处的参数 `f(1, 2)`
		- 这里的参数具有实际意义，是真实拿来运算的值
- 除了上述分类方法，我们还有一些别的类型的参数

<!--v-->

## 可选的参数

- 还记得 `print` 吗，我们可以加上 `, end=""` 来去除默认的结尾换行
- 但是如果我们定义了一个 `my_print(var, end)` 而不写 end 会如何呢

**演示** my_print

- 我们会发现，在第二个语句中发生了错误

```py
TypeError: my_print() missing 1 required positional argument: 'end'
```

- 什么是 `positional argument`?

<!--v-->

## 可选的参数 (cont'd)

**演示** 可选参数

- Python 函数支持的参数按照**调用时的要求**可以有四种，我们只简单介绍两种
- 注意，我们这里都在说**调用时**参数的要求，所以这里的参数都是指调用时的实际参数 (argument)
	- 位置 (positional) 参数：我们之前写的都是位置参数，顾名思义，依靠**出现的先后顺序**来决定是哪个参数
	- 关键字 (keyword) 参数：直接按照**形参的名字**来确定参数
	- 默认 (default) 参数：也就是可以省略的参数
		- 如果要使用，需要在定义的时候给形参指定**默认值**，从而可以在调用中省略，也可以覆盖，适合大量重复的参数
- 他们很多也可以混合使用，这体现了 Python 的灵活性
- 但是，某些情况是不允许的！

<!--v-->

## 可选的参数 (cont'd)

```py []
# 假设定义了 def key_func2(x, y, z, a, b, c)
key_func(1, z=3, 2, x=1, b=3, 4) # 这是不允许的
```

- 思考：为什么不允许位置参数出现在关键字参数后面？
	- 实际上是为了防止 **歧义**，同时提高代码 **可读性**，例如，上面的例子就非常混乱，如何分配 `1, 2, 4`？人类都得找很多遍才能排除已有的关键字，计算机代码就更复杂了，这是不必要的，会带来不必要的计算复杂性。

<!--s-->

# 04. 作用域

<!--v-->

## 作用域：发挥作用的区域

**演示** 下面代码有一点点小迷惑，因为他有两个相同名字的变量，而且输出了四次

```py [1,6|7,10,13,16]
which_li_hua = "高考英语卷中"
# 我们都知道，李华是一个很有名的人物，他在高考英语卷中出现了很多次
# 我们看看不同人提到李华时会想到什么

def ShanghaiTech(): # 假设上海科技大学里来了一个李华（假设上科大人尽皆知）
    which_li_hua = "上海科技大学"
    print("上科大的", which_li_hua) # 上科大的人第一反应肯定是上科大的李华

def SUSTech(): # 假设隔壁大学没有李华
    print("隔壁大学", which_li_hua) # 隔壁大学人的第一反应肯定是高考英语卷中的李华

# 外面的人（最外层）没有听说过别的李华
print("外面的人", which_li_hua) # 自然会认为这个李华是高考英语卷中的李华
ShanghaiTech() # 调用 ShanghaiTech 函数
SUSTech() # 调用 SUSTech 函数
print("外面的人", which_li_hua) # ShanghaiTech 的李华不会影响外面的人心中的李华
```

<!--v-->

但是我们可以完全用我们日常生活来理解输出的逻辑

```py [0|1,12-13|14,5-7|15,9-10|16|0]
which_li_hua = "高考英语卷中"
# 我们都知道，李华是一个很有名的人物，他在高考英语卷中出现了很多次
# 我们看看不同人提到李华时会想到什么

def ShanghaiTech(): # 假设上海科技大学里来了一个李华（假设上科大人尽皆知）
    which_li_hua = "上海科技大学"
    print("上科大的", which_li_hua) # 上科大的人第一反应肯定是上科大的李华

def SUSTech(): # 假设隔壁大学没有李华
    print("隔壁大学", which_li_hua) # 隔壁大学人的第一反应肯定是高考英语卷中的李华

# 外面的人（最外层）没有听说过别的李华
print("外面的人", which_li_hua) # 自然会认为这个李华是高考英语卷中的李华
ShanghaiTech() # 调用 ShanghaiTech 函数
SUSTech() # 调用 SUSTech 函数
print("外面的人", which_li_hua) # ShanghaiTech 的李华不会影响外面的人心中的李华
```

<!--v-->

## 作用域：发挥作用的区域

- 作用域(Scope)：发挥作用的区域，与缩进的代码块紧密相连
	- 我们定义的变量、函数等等都有它发挥作用的区域，目前你可以简单地认为
		- 定义在最外层的（无缩进）就是全局变量，作用范围为全局
		- 定义在有缩进的区域就是局部变量，作用范围为当前代码块
	- 全局变量和局部变量之间如果重名，优先使用局部变量（前提是**先**定义了局部变量）

**演示** 错误的优先局部变量

- 变量的作用域和作用域的查找是非常复杂的，这里由于时间问题只简单的提了一嘴，大家可以在 SI 100B 正课学到完整的作用域知识，目前大家在编写代码的过程中只需要尽可能避免复杂的重名即可

<!--s-->

## 05. 上手写！圆的周长面积计算器～

```py
>>> r = 
<<< 5
>>> Area of circle: 78.53981633974483
>>> Circumference of circle: 31.41592653589793
```

<!--v-->

## 05. 上手写！圆的周长面积计算器～  (cont'd)

```py []
import math # 导入 math 库，可以使用 math.pi

def area_of_circle(radius=1): # 默认半径为 1
    return math.pi * radius ** 2

def circumference_of_circle(radius=1): # 默认半径为 1
    return 2 * math.pi * radius

r = int(input("r = "))
area = area_of_circle(r) # 通过位置参数传入半径
circumference = circumference_of_circle(radius=r) # 通过关键字参数传入半径

print("Area of circle: ", area)
print("Circumference of circle: ", circumference)
```

<!--s-->

## Takeaway Message

<!--s-->

# End