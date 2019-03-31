"""
    Python 内建了 `map()` 和 `reduce()` 函数;

    `map()` 函数接收两个参数，一个是函数，一个是 `Iterable`，`map`将传入的函数依次
    作用到序列的每个元素，并把结果作为新的 `Iterator` 返回
"""

def f(x):
    return x * x

def main():
    # map() 传入的第一个参数是 f ,即函数对象本身
    # 由于结果 r 是一个 Iterator ,Iterator 是惰性序列，因此通过 list() 函数让它把
    # 整个序列都计算出来并返回一个 list 。

    r = map(f,[1,2,3,4,5,6,7,8,9])
    print('type(r):', type(r))
    print(list(r))

    # 可能会想，不需要 map() 函数，写一个循环，也可以计算出结果：
    L = []
    for n in [1,2,3,4,5,6,7,8,9]:
        L.append(f(n))
    print(L)
    
    """
        从上面的循环代码，能一眼看明白"把 f(x) 作用在 list 的每一个元素并把结果生成一个新的list"

        所以, `map()` 作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的
        f(x) = x2 ，还可以计算 任意复杂的函数，比如，
        可以把这个 list 所有数字转换为字符串：
    """
    
    numstr = list(map(str,[1,2,3,4,5,6,7,8,9]))
    print('numstr: {} '.format(numstr))

    """
        reduce 的用法：
        `reduce` 把一个函数作用在一个序列 `[x1,x2,x3,...]` 上，这个函数必须接收两个
        参数， `reduce` 把结果继续和序列的下一个元素做累积计算，其效果就是：
        reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
    """
    # 比如说对一个序列求和，就可以用 `reduce` 实现
    from functools import reduce
    def add(x,y):
        return x + y

    print('add(1,2): {} '.format(add(1,2)))
    print('reduce(add,[1,3,5,7,9]):  {} '.format(reduce(add,[1,3,5,7,9])))

    # 如果把序列 [1,3,5,7,9] 变换成 整数 13579 ，reduce 就可以派上用场：

    def fn(x,y):
        return x * 10 + y
    
    print('reduce(fn,[1,3,5,7,9]): {} '.format(reduce(fn,[1,3,5,7,9])))

    # 考虑 str 是一个序列，对上面的例子稍加改动，配合 map() ，我们就可以写出把 str 
    # 转换成 int 的函数
    def char2num(s):
        digints = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digints[s]

    print('reduce(fn,map(char2num,"13579")): {} '.format(reduce(fn,map(char2num,'13579'))))
    
    print('#############################################')
    # 整理成一个 `str2int` 的函数就是：
    DIGINT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def str2int(s):
        def fn(x,y):
            return x * 10 + y
        def char2num(s):
            return DIGINT[s]
        return reduce(fn,map(char2num,s))

    print('-----------------------------------------------')
    # 可以用 lambda 函数进一步简化成：
    DIGINT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(s):
        return DIGINT[s]

    def str2int(s):
        return reduce(lambda x,y : x * 10 + y, map(char2num,s))



    """
        利用 `map()` 函数，把用户输入的不规范的英文名字，编程首字母大写，
        其他小写的规范名字。
        输入： ['adam','LISA','barI']
        输出： ['Adam','List','Bart']
    """

    def normalize(name):
        # i = 0
        # while i < len(name):
        #     if i == 0:
        #         name[i] = name[i].upper()
        #     else:
        #         name[i] = name[i].lower()  
        #     i += 1
        # return name
        # return name.title()
        return name.capitalize()
        

    print('------------------------- 测试 -----------------------------')   
    # 测试:
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    """
        Python 提供的 sum() 函数可以接受一个 list 并求和，请编写一个 prod() 函数，
        可以接受一个 list 并利用 reduce() 求和：
    """
    print('prod()---> 接受一个 list 并利用 reduce() 求和')
    def prod(L):
        return reduce(lambda x,y : x * y ,L)

    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')



    """
        利用 map 和 reduce 编写一个 str2float 函数，
        把字符串 '123.456' 转换为浮点数 123.456

    """
    def str2float(s):
        list = s.split('.')
        print('list:  {} '.format(list))

        """
            1.字符串切割，获得一个 list ,两个元素
            2.
        """

        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        def char2num(s):
            return DIGITS[s]
        
        int_num = reduce(lambda x,y : x * 10 + y,map(char2num,list[0]))
        decimal_num = reduce(lambda x,y : x / 10 + y,map(char2num,list[1][::-1])) / 10

        return int_num + decimal_num

    print('str2float(\'123.0456\') =', str2float('123.0456'))
    if abs(str2float('123.0456') - 123.0456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')




if __name__ == "__main__":
    main()