
<blockquote class="blockquote-center">沉迷尤克里里电影和美丽花衣裳的程序媛要开始LeetCode了，在Java和Python之间义无反顾选择了Python，毕竟要竭尽全力减轻负担啊哈哈。快速自学记录一下语法特别之处吧╮(─▽─)╭
cr: [廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)</blockquote>

<!-- more -->

## 编码
ASCII（1个字节）：美国人儿那套；
Unicode（2个字节）：把所有语言都统一到一套编码里，这样就不会再有乱码问题了（浪费空间）；
UTF-8（可变长编码）：
UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间。
UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

## 字符串
普通str，以Unicode表示；
前缀'r'，防止转义；
前缀'b'，bytes类型，一个字节；
encode()：如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes；
decode()：如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes，需把bytes变为str；
.decode('utf-8', errors='ignore')：bytes中包含无法解码的字节会报错，这样忽略掉错误；


## dict和set
### dict和list
和list比较，dict有以下几个特点：
1. 查找和插入的速度极快，不会随着key的增加而变慢；
2. 需要占用大量的内存，内存浪费多。
而list相反：
1. 查找和插入的时间随着元素的增加而增加；
2. 占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

### set和dict
1. set和dict唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
2. 相同点：key必须是不可变对象;
3. 补充：使用set过滤重复数组时，由于list是可变对象，不能作为set的元素，可以先将其转化为不变的tuple,最后再依次转换回list。 `list( map(list, res) )`


## 函数
### 定义函数
如果有必要，可以先对参数的数据类型做检查；
函数可以同时返回多个值，但其实就是一个tuple。
空函数：pass语句

### 函数参数
默认参数：一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
可变参数和关键字参数：
```*args```是可变参数，args接收的是一个tuple；
```**kw```是关键字参数，kw接收的是一个dict。
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过```**kw```传入：```func(**{'a': 1, 'b': 2})```。
使用\*args和```**kw```是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符\*，否则定义的将是位置参数。```def person(name, age, *, city, job):```

### 尾递归
在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
Python标准的解释器没有针对尾递归做优化。


## 高级特性
### 切片
 L[m:n]：取一个string、list或tuple的部分元素；
 s[::-1]：反转字符串

### 迭代
```for ... in```：只要是可迭代对象，无论有无下标，都可以迭代。判断一个对象是否可迭代对象可通过collections模块的Iterable类型判断：
```from collections import Iterable>>> isinstance('abc', Iterable)```

默认情况下，dict迭代的是key。如果要迭代value，可以用```for value in d.values()```，如果要同时迭代key和value，可以用```for k, v in d.items()```
实现下标循环：
```for i, value in enumerate(['A', 'B', 'C']):...     print(i, value) ```

### 生成器generator
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素。
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator。在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
generator函数的“调用”实际返回一个generator对象。
用for循环调用generator时拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中。

### 迭代器iterator
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列（数据流）；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的。

## 函数式编程
### 高阶函数
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
map()函数：接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
reduce：把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
filter()：从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
排序：```sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)```

### 匿名函数
lambda，只能有一个表达式，不用写return，返回值就是该表达式的结果。
不必担心函数名冲突。

### 偏函数
当函数的参数个数太多，需要简化时，使用```functools.partial```可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

## Python2与Python3
### 迭代器
**range与xrange**
python3中已经没有xrange函数了，其中的range已经是使用xrange的机制实现，所以直接用range就好啦。
**其它**
1. 字典对象的 dict.keys()、.items、dict.values() 方法都不再返回列表，而是以一个类似迭代器的 "view" 对象返回。而之前的iterkeys()等函数都被废弃。同时去掉的还有 dict.has_key()，用 in替代它吧 。
2. 高阶函数 map、filter、zip 返回的也都不是列表对象了。
3. Python2的迭代器必须实现 next 方法，而 Python3 改成了 __next__

### 数据类型
1. Python3去除了long类型，只有一种整型【int】，但其行为和python2的long一致；
2. Python3新增了bytes类型，分别用 str 表示字符串，byte 表示字节序列，任何需要写入文本或者网络传输的数据都只接收字节序列，这就从源头上阻止了编码错误的问题。
{% asset_img bytes类型.png %}

### 作用域
>变量引用顺序：当前作用域局部变量 -> 外层作用域变量 -> 当前模块中全局变量 -> Python内置变量
1. **global**
a. 在函数或其他局部作用域中要对**全局变量**做修改，则需要在局部使用global再次声明该全局变量。
b. 不做修改时不必使用global声明。
c. 由于全局性，函数执行完毕后不回销毁使用global修饰的变量。
2. **nonlocal**
a. Python3在嵌套函数中可以使用关键字nonlocal将变量声明为非局部；
b. 适用于在一个局部作用域中的局部作用域使用，绑定一个外层（非全局）变量。

### 比较函数
python2中可以使用函数cmp来比较，python3中这个函数也废掉了，那应该用啥咧~~
