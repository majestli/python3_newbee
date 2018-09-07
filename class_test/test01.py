class myClass:
    '''this is test'''
    i=12345
    def f(self):
        return 'hello world'


x=myClass()

print("myClass 类的属性 i:",x.i)
print("myClass 类的方法 f:",x.f())
