from 学生管理系统 import tool
class Teacher(object):
    def __init__(self,name,password):
        self.name=name
        self.password=tool.encrypt_password(password)
class Student(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
