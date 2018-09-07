import socket
import  sys


# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
port =9999
serversocket.bind((host,port))
serversocket.listen(5)
ip=serversocket.getsockname()
print('ip addr :%s'%str(ip))


while True:
    clientsocket,addr=serversocket.accept()
    print("connect addr:%s" %str(addr))
    msg='welcome access cainiao!'+"\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()


#python单引号与双引号的区别
#使用双引号时，字符串中有单引号，为避免使用转义\
#同理使用单引号时，

#这就是Python易用性和人性化的一个极致体现，当你用单引号' '定义字符串的时候，它就会认为你字符串里面的双引号"
# "是普通字符，从而不需要转义。反之当你用双引号定义字符串的时候，就会认为你字符串里面的单引号是普通字符无需转义

#三个单号好与三个双引号
# 得到我们期望的一行一个名字的输出格式呢？这就是3个引号的作用了
#虽然我们也可以通过给字符串加上\n实现
#而且使用3个引号还有一个特别棒的作用就是：加注释！
