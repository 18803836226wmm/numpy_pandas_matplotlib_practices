class Cat:
    def __init__(self,name):
        self.name=name
        # 如果对象是局部的 那么函数执行完毕，自动调用对象额del方法
        # 如果对象是全局的 那么执行完毕，自动调用对象额del方法
    def __del__(self):
        print("%s 销毁了"% self.name)
    # 如果在开发过程中 希望使用print输出对象变量时，能够打印自定义的内容，就可以使用__str__这个内置方法
    # 这个方法必须返回一个字符串 不能返回其他类型
    def __str__(self):
        return "我是一只%s" % self.name
cc=Cat("aa")
# 当把对象直接放在print里面，实现的是对象在内存的地址编号，
print(cc)

class Calc:
    def __init__(self,oper="+"):
        self.oper=oper
    def calc(self,a,b):
        if self.oper=="+":
            return a+b
        elif self.oper=="-":
            return a-b
        elif self.oper=="*":
            return a*b
        elif self.oper=="/":
            if b!=0:
                return a/b
            else:
                return None
        else:
            return None
c=Calc()
print(c.calc(1,2))

