'''示例3: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)”
但发现新函数只在第一次被调用，且原函数多调用了一次'''

def deco(myfuc):
    print('before myfunc')
    myfuc()
    print('after myfunc')
    return myfuc

@deco
def myfunc():
    print('myfunc is called')

myfunc()
myfunc()


