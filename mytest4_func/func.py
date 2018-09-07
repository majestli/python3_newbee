def say_hello(a,b):
    if a> b:
        print('a >b')
    elif a==b:
        print('a==b')
    else:
        print('a<b')
    print('hello world!')



say_hello(3,5)
x=5
y=2
say_hello(x,y)

def say(message,times=1):
    print(message * times)
say('hello')
say('world',5)
