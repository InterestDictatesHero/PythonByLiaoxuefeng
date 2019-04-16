"""
    排序算法
    `Python`内置的`sorted()`函数就可以对`list`进行排序

    `sorted()` 函数是一个高阶函数，它还可以接收一个 `key` 函数来实现自定义的排序，
    例如按绝对值大小排序；
    `key`指定的函数作用于`list`的每一个元素上，并根据`key`函数返回的结果进行排序。

    默认情况下，对字符串排序，是按照`ASCII` 的大小比较的，
    由于'Z' < 'a',结果，大写字母 'Z' 会 排在 'a' 的前面

    要进行反向排序，不必改动`key`函数，可以传入第三个参数 'reverse = True'
"""
def main():
    print("sorted([36, 5, -12, 9, -21]):  {}".format( sorted([36,5,-12,9,-21])))

    print('sorted([25,5,-12,9,-21],key = abs)  : {}'.format(sorted([25, 5, -12, 9, -21], key=abs)))

    print('sorted([\'bob\',\'about\',\'Zoo\',\'Credit\']):  {}'.format(sorted(['bob', 'about', 'Zoo', 'Credit'])))

    # 忽略大小写进行排序
    # 可以先把字符串都变为大写(或者都变成小写)，再比较
    print('sorted([\'bob\', \'about\', \'Zoo\', \'Credit\'],key = str.lower) : {}'.format(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)))
    
    print('sorted([\'bob\', \'about\', \'Zoo\', \'Credit\'],key = str.lower,reverse = True) : {}'.format(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)))

    """
        练习：

        假设我们用一组tuple表示学生名字和成绩：

        L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
        请用sorted()对上述列表分别按名字排序：
    """
    def by_name(t):
        return t[0]
    
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key=by_name)

    print(L2)

    # 按照成绩从高到低排序
    def by_score(t):
        return -t[1]
    
    L2 = sorted(L, key=by_score)

    print(L2)

if __name__ == "__main__":
    main()
