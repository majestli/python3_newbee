class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print('hello,how are you?,my name is',self.name)
p=Person('swaroop') #先实例化一个对象，然后将指针负责给p，引用
p.say_hi()

