"""学习目标
1.面向对象的3大特点 ：封装（根据职责将属性方法封装到一个抽象的方法中）、继承（实现代码的重复使用）、多态（不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度）
2。掌握继承的语法 :子类拥有父类的所有方法和属性
3。掌握方法的重写
4。掌握类属性和类方法的使用"""
"""面向对象进阶 --封装
一：类的私有属性：对象不希望公开的属性
   私有方法：对象不希望公开的方法
   定义方式：在属性名、方法名前 增加两个下划线，私有方法和私有属性 只能在类的内部访问 类的外部无法访问
   """
class woman:
    def __init__(self,weight=0,age=0,name=''):
        self.__weight=weight
        self.__age=age
        self.name=name
    def __secret(self):
        print("我的体重是%d，年龄是%d" %(self.__weight,self.__age))
    def show_secret(self):
        self.__secret()
# 当父类的方法实现不能满足子类额需求时 可以对方法进行重写
# 重写有两种情况 1，覆盖父类的方法 2，对父类方法进行扩展:在子类中重写父类方法，在需要的位置使用super（）.父类来调用父类方法的执行
# 如果在开发中，父类方法的实现和子类的方法实现，完全不同，就可以使用覆盖的方式，在子类中重新编写父类方法 相当于在子类中定义了一个和父类同名的方法且实现 重写之后，
# 运行只会调用子类的重写方法，不会调用父类封装的方法
"""子类对象不能在自己的方法内部直接访问父类的私有属性或私有方法，可以通过父类的共有方法间接访问到私有属性或私有方法
私有属性方法：、是对象的隐私，不对外公开 外界以及子类都不能直接访问
私有属性、方法通常用于做一些内部的事情
"""

class animal:
    def sleep(self):
        print("睡")
    def eat(self):
        print("吃")
class dog(animal):
    def run(self):
        print("跑")
    def eat(self):
        print("吃肉")
d=dog()
print(d.eat())

class animal2:
    def sleep(self):
        print("animal2睡")
    def eat(self):
        print("吃")
class Cat2(animal2):
    def run(self):
        print("跑")
    def sleep(self):
        super().sleep()
        print("睡的更堵")
c2=Cat2()
c2.sleep()

