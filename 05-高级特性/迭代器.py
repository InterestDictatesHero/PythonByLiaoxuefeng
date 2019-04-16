"""
#                             _______________________________________  
#                            /  ___________________________________  \
#     _--""""--_            /  /_/_/_/_/_|_|_|_|_|_|_|_|_|_\_\_\_\_\  \
#    /          \          /  /_/_/_/_J__L_L_L_|_|_|_J_J_J__L_\_\_\_\  \
#   /\          /\        /  /_/_/_J__L_J__L_L_|_|_|_J_J__L_J__L_\_\_\  \
#   L ""-____-"" J       /  /_/_J__L_J__L_J_J__L_|_J__L_L_J__L_J__L_\_\  \
#   \            /      /  /_/__L_/__L_J__L_J__L_|_J__L_J__L_J__\_J__\_\  \
#    \_        _/      /  /_J__/_J__/__L_J__|__L_|_J__|__L_J__\__L_\__L_\  \
#  _--"""""--_"       /  /  F /  F J  J  |  F J  |  F J  |  F  F J  \ J  \  \
# /           \      /  /--/-J--/--L--|--L-J--J--|--L--L-J--|--J--\--L-\--\  \
# /\           /\    /  /__/__L_J__J___L_J__J__|__|__|__L__L_J___L__L_J__\__\  \
# L ""-_____-"" J   /  /  /  /  F  F  J  J  |  |  |  |  |  F  F  J  J  \  \  \  \
# \             /  /  /--/--/--/--J---L--|--|--|--o--|--|--|--J---L--\--\--\--\  \
# \_         _/  /  /__/__J__J___L__J___L__L__L__|__J__J__J___L__J___L__L__\__\  \
#   "--___--"   /  /  /   F  F  J   F  J  J   F  |  J   F  F  J   F  J  J   \  \  \
#              /  /--/---/--J---L--J---L--|--J---|---L--|--J---L--J---L--\---\--\  \
#             /  /__J___/___L__/___L__J___L__J___|___L__J___L__J___\__J___\___L__\  \
#            /  /   F  J   /  J   J   |  J   J   |   F   F  |   F   F  \   F  J   \  \
#           /  /---/---L--J---L---L---L--|---|---|---|---|--J---J---J---L--J---\---\  \
#          /  /___/___/___L__J___J___J___|___|___|___|___|___L___L___L__J___\___\___\  \
#         /  /   /   /   /   F   F   F   F   F   |   J   J   J   J   J   \   \   \   \  \
#        /  /___/___J___J___J___J___J____L___L___|___J___J____L___L___L___L___L___\___\  \
#       /  /   /    F   F   F   |   |   J    F   |   J    F   |   |   J   J   J    \   \  \
#      /  /___J____/___/___J____L___L___|___J____|____L___|___J___J____L___\___\____L___\  \
#     /  /    F   /   J    F   J   J    |   J    |    F   |    F   F   J    F   \   J    \  \
#    /  /____/___J____L___/____L___|____L___|____|____|___J____|___J____\___J____L___\____\  \
#   /  /    /    F   /   J    J    F   J    F    |    J    F   J    F    F   \   J    \    \  \
#  /  /____/____/___J____L____|____L___J____L____|____J____L___J____|____J____L___\____\____\  \
# /                                                                                             \
# /_______________________________________________________________________________________________\
# |                                                                                               |
# |                                     天下大同                                                       |
# |_______________________________________________________________________________________________|

    可以直接作用于 `for` 循环的数据类型有以下几种:
    一类是集合数据类型，如 `list`、`tuple`、`dict`、`set`、`str` 等
    一类是 `generator`，包括生成器 和 带 `yield` 的 gererator function

    这些可以直接作用于 for 循环的对象统称为 可迭代对象: Iterable
    可以使用 `isinstance()` 判断一个对象是否是 `Iterable` 对象
"""

from collections import Iterable

def main():
    print('isinstance([],Iterable):',isinstance([],Iterable))
    print('isinstance({},Iterable):',isinstance({},Iterable))
    print('isinstance("abc",Iterable):',isinstance('abc',Iterable))
    print('isinstance((x for x in range(10)),Iterable):',isinstance((x for x in range(10)),Iterable))
    print('isinstance(100,Iterable):',isinstance(100,Iterable))

    """
        `生成器`不但可以作用于 `for` 循环，还可以被 `next()` 函数不断调用并返回下一个值，
        直到最后抛出 `StopIteration` 错误表示无法继续返回下一个值

        可以被 `next()` 函数调用并不断返回下一个值得对象称为迭代器： `Iterator`

        可以使用 `isinstance()` 判断一个对象是否是 `Iterator` 对象
    """
    from collections import Iterator
    print('isinstance([],Iterator):',isinstance([],Iterator))
    print('isinstance({},Iterator):',isinstance({},Iterator))
    print('isinstance("abc",Iterator):',isinstance('abc',Iterator))
    print('isinstance((x for x in range(10)),Iterator):',isinstance((x for x in range(10)),Iterator))

    print('-----------------------------------------------------------------')
    """
        生成器都是 `Iterator`对象，但 `list`、`dict`、`str`虽然是 `Iterable`，却
        不是 `Iterator` 

        把 `list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用 `iter()` 函数
    """    
    print('isinstance(iter([]),Iterator):  ',isinstance(iter([]),Iterator))
    print('isinstance(iter(\'abc\'),Iterator):  ',isinstance(iter('abc'),Iterator))


    """
        这是因为 Python 的 Iterator 对象表示的是一个数据流，
        Iterator 对象可以被 next() 函数调用并不断返回下一个数据，直到没有数据是抛出
    StopIteration 错误。
        可以把这个数据流看做一个有序序列，但我们却不能提前知道序列的长度，只能不断通过
    next() 函数实现按需计算下一个数据，所以 Iterator 的计算式惰性的，只有在需要返回下
    一个数据时它才会计算。

        Iterator 甚至可以表示一个无限大的数据流，例如全体自然数。
        而使用 list 是永远不可能存储全体自然数的
    """

    """
        1. 凡是可作用于 `for` 循环的对象都是 `Iterable`类型;
        2. 凡是可用于 `next()` 函数的对象都是 `Iterator` 类型，它们表示一个惰性计算的序列；
        3. 集合数据类型 如 `list`、 `dict`、 `str` 等是 `Iterable` 但不是 `Iterator`,
           不过可以通过 `iter()` 函数获得一个 `Iterator` 对象。
    """

if __name__ == "__main__":
    main()