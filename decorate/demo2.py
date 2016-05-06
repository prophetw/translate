'''
装饰函数的参数是被装饰的函数对象，返回原函数对象
装饰的实质语句: myfunc = deco(myfunc)
'''
def deco(myfuc):
    print('before myfunc')
    myfuc()
    print('after myfunc')
    return myfuc


def myfunc():
    print('myfunc is called')

myfunc = deco(myfunc)

myfunc()
myfunc()


