"""
    生成器
    如果列表元素可以按照某种算法推算出来，可以在循环的过程中不断推算出后续的元素
    在Python中，这种一边循环一边计算的的机制，称为生成器 : generator
"""

# 斐波拉契数列
# 定义 generator 的另一种方法，如果一个函数定义中包含 `yield` 关键字，那么这个
# 函数就不是一个普通函数，而是一个 generator;
def fib(max):
    n,a,b = 0,0,1
    while n < max :
        # print(b)
        yield b
        a,b = b , a + b
        n = n + 1
    return 'done'


def main():
    # 1. 只要把 一个列表生成式 的 [] 改为 (),就创建了一个 generator
    # L = [x * x for x in range(10)]
    # print('L: ', L)
    # print('-----------------------')
    # g = (x * x for x in range(10))
    # # print('g : ', g)
    # for n in g:
    #     print(n)

    """
        我们创建了一个 `generator` 后，基本上永远不会调用 next(),
        而是通过 for 循环来迭代它，并且不需要关心 `StopIteration` 的错误
        generator 非常强大
        如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，
        还可以用函数来实现
    """

    # print(fib(6))

    # 要把 `fib` 函数变成 `generator` , 只需要把 `print(b)` 改为 `yield b`就可以了

    # 变成 `generator` 的函数，在每次调用 `next()` 的时候，遇到 `yield`语句返回，
    # 再次执行是从上次返回的 `yield` 语句处继续执行

    def odd():
        print('step 1')
        yield 1
        print('step 2')
        yield 2
        print('step 3')
        yield(5)

    # 调用改generator时，首先要生成一个 generator 对象，然后用 next() 函数不断获得
    # 下一个返回值
    o = odd()
    print(next(o))
    print(next(o))
    print(next(o))

    print('---------------- 我是分割线 --------------------------')

    for n in fib(6):
        print(n)

    print('---------------- 我是分割线 --------------------------')

    g = fib(6)
    while True:
        try:
            x = next(g)
            print('g:',x)
        except StopIteration as e:
            print('Generator return value: ', e.value)
            break


    # 杨辉三角
    def triangles():
        n = 1
        list = []
        temp = []
        request = []
        i = 0
        while n <= 10:
            while i < n:
                if (i == 0) or (i == n - 1):
                    temp.insert(i,1)
                else:
                    temp.append(list[i - 1] + list[i])
                i += 1

            list = temp
            # request.append(temp)
            yield temp
            n += 1
            i = 0
            temp = []
        # return request

    n = 0
    results = []
    for t in triangles():
        print(t)
        results.append(t)
        n = n + 1
        if n == 10:
            break
    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')
if __name__ == "__main__":
    main()