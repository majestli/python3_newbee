import  ctypes
import os
lib=ctypes.cdll.LoadLibrary(os.getcwd()+ "/libpycall.so")
a=lib.foo(1,3)
print(a,end='')
print("finish")
