
"""不同的子类，调用相同的父类方法，产生不同的结果
多态的前提，不同的子类俩源于同一个父类，子类会覆盖父类的方法"""
class animal:
    def food(self):
        pass
    def eat(self):
        self.food()
class dog(animal):
    def food(self):
        print("吃肌肉")
class cattle(animal):
    # 子类会覆盖父类的方法
    def food(self):
        print("吃草")
d=dog()
d.eat()
c=cattle()
c.eat()