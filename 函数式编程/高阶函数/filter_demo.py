"""
    Python 内建的 ` filter() ` 函数用于过滤序列；
    和 `map()`类似，`filter()`也接收一个函数和一个序列。
    和 `map()`不同的是，`filter()` 把传入的函数椅子作用于每个元素，然后根据
    返回值是 `True` 还是 `False` 决定保留还是对其该元素

    * 注意
    `filter()` 函数返回的是一个 `Iterator` ，也就是一个惰性序列，
    所以要强迫 `filter()` 完成计算结果，需要用 `list()`函数 获得所有结果并返回`list`
"""

# 在一个list中，删除偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

# 用filter求素数
# 先构建一个从3开始的奇数序列
# 注意这是一个生成器，并且是一个无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始化序列
    while True:
        n = next(it) # 返回序列的第一个数
        
        yield n
        it = filter(_not_divisible(n),it)
        
def is_palindrome(n):
    sum = 0
    temp = n
    while temp // 10 > 0:
        quotient = temp // 10 # 商
        remainder = temp % 10 # 余数
        temp = quotient
        sum = sum * 10 + remainder * 10
    sum += temp 
    return sum == n

def main():

    # 过滤奇数
    print('list(filter(is_odd,[1,2,3,4,5,6,7,8,9])) :  ',list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

    # 删掉序列中的空字符串：
    print('list(filter(not_empty,[\'A\',\'\',\'B\',\'b\',None,\'C\',\'  \'])) -->   {}'.format( list(filter(not_empty,['A','','B','b',None,'C','  ']))))

    print('----------我是(*╹▽╹*)的分割线----------')
    # 由于 `primes()` 也是一个无限序列，所以调用的时候需要设置一个退出循环的条件：
    # 打印 1000 以内的素数：
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
    # for n in _odd_iter():
    #     if n < 100:
    #         print(n)
    #     else:
    #         break
    

    """
        练习
        回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
        请利用filter()筛选出回数：
    """
    print('--------------------------------------------')
    # output = filter(is_palindrome, range(1, 100))
    # print('1~100:', list(output))
    print('--------------------------------------------')
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')

if __name__ == "__main__":
    main()