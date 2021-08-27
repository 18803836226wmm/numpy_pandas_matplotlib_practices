"""面向对象进阶--类属性和类方法  不需要创建对象，通过类名的方式就可以访问的属性或者点用类的方法"""
# 类方法用@classmethod的方法为类方法
# 类方法的参数为cls，在类方法内部通过cls.类属性或者cls.类方法 来访问同一个类中的其他类属性和类方法
# 类方法不需要实力话就可以调用，类方法只能访问同一个类中的类属性和类方法

# 普通方法访问类属性或者类方法
# 在普通方法中通过类名.属性或者类名.类方法来访问类属性和类方法

# 如果需要在类中封装一个方法 这个方法既不需要访问实例属性，或者调用实例方法也不需要访问类属性或者调用类方法，这个时候可以把这个方法封装成一个静态方法
# 1。用@staticmethod 修饰为静态方法
# 2。静态方法是独立存在的 不能访问类或者实例的任何属性和方法
# 3。通过类名.静态方法 调用静态方法
class A(object):
    # name 为类属性
    name="Tom"
    # show_name为类方法
    @classmethod
    def show_name(cls):
        print(cls.name)
    # show_help为类的静态方法
    @staticmethod
    def show_help():
        print("静态方法")
    # set_name为普通方法
    def set_name(self,name):
        A.name=name
A.show_name()
a=A()
a.set_name("mm")
A.show_name()
A.show_help()



list_e = [(e, f * f) for e in range(3) for f in range(5, 15, 5)]
print(list_e)