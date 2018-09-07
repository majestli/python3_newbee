#coding = UTF-8


class Robot:
    """表示有一个带有名字的机器人"""
    population=0

    def __init__(self,name):
        """初始化数据"""
        self.name=name
        print("initializing {}".format(self.name))
        Robot.population+=1
    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))
        Robot.population-=1
        if Robot.population==0:
            print("{}was the last one".format(self.name))
        else:
            print("there are still {:d} robots working".format(Robot.population))
    def  say_hi(self):
        """ 快来自机器人的问候"""
        print("Greetings,my master call me {}".format(self.name))
    @classmethod
    def how_many(cls):
        """打印当前的人口数量"""
        print("we have {:d}  robots".format(cls.population))



droid1=Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 =Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here \r\n")
print("Robots have finished their work")
droid1.die()
droid2.die()
Robot.how_many()
