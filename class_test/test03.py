class people:
    name=''
    age=0
    __weigth=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weigth=w
    def speak(self):
        print("%s say: i'm %d old"%(self.name,self.age))

#p=people('runoob',10,30)
#p.speak()

class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print("%s say: i'm %d old, i'm learn at %d" %(self.name,self.age,self.grade))

s =student('Ken',10,60,3)
s.speak()
