def main():
    
    # print([x * x for x in range(1,11) if x % 2 == 0])

    # 导入 os 模块
    # import os 
    # print([d for d in os.listdir('.')])

    # for 循环可以同时使用两个甚至多个变量，比如 dict 的item() 可以同时迭代key 和 value
    d = {'x':'A','y':'B','z':'C'}
    for k,v in d.items():
        print(k,' = ', v)

    print('-------------------------------------')

    print([k + ' = ' + v for k,v in d.items()])
    
    print('========================================')
    
    L = ['Hello','World','IBM','Apple']
    print([s.lower() for s in L])

    """
        练习
        如果 list 中既包含字符串，又包含整数，由于非字符串类型没有 lower() 方法，所以
        列表生成式会报错：

        提示：内建的 `isinstance` 函数 可以判断一个变量是不是字符串
    """
    x = 'abc'
    y = 123
    print('isinstance(x,str): ',isinstance(x,str))

    print('isinstance(y,str): ',isinstance(y,str))

    # 练习测试
    L = ['Hello','World',18,'Apple',None]

    L2 = [s.lower() for s in L if isinstance(s,str) == True]
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过！')
    else:
        print('测试失败！')
if __name__ == "__main__":
    main()