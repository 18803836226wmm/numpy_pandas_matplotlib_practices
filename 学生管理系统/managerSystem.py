from 学生管理系统 import file_manager
from 学生管理系统.model import *
name=''
class StudentManager(object):
    # 为啥名字要为空
    name=''
    def __init__(self):
        #存储学院数据列表
        self.student_list=[]
    # 程序入口函数
    def run(self):
        # 1。加载文件里面的学员函数
        # self.load_student()
        while True:
            # 显式功能菜单
            self.show_menu()
            # 用户输入目标功能序号
            menu_num=input("请输入你需要的功能序号")
            # 根据不同的序号，执行不同的功能
            if menu_num=='1':
                self.add_student()
            elif menu_num=='2':
                self.del_student()
            elif menu_num=='3':
                self.modify_student()
            elif menu_num=='4':
                self.search_student()
            elif menu_num=='5':
                self.show_student()
            elif menu_num=='6':
                self.save_student()
            elif menu_num=='7':
                break
            else:
                print("输入错误")
    # 系统功能函数 2。1显示功能菜单，这种方法一般需要使用静态方法
    @staticmethod
    def show_menu():
        content=file_manager.read_file('students_pages.txt')
        print(content)
    def add_student(self):
        # 1。用户输入信息
        name=input("请输入你的姓名")
        age=input("请输入你的年龄")
        gender=input("请输入你的性别")
        # 2创建学员对象，将信息传递进去
        student=Student(name,age,gender)
        # 3.将学生添加到学员列表中
        self.student_list.append(student)
        print(self.student_list)
        print(student)
    # 删除
    def del_student(self):
        del_name=input("请输入要删除的学生的名字")
        #首先要遍历 有的画就删除，没有的话就提示
        for i in self.student_list:
            if i.name==del_name:
                self.student_list.remove(i)
                break
        else:
            print("查无此人")
        print(self.student_list)
    # 修改
    def modify_student(self):
        modify_name=input("输入要修改的学生信息的姓名")
        for i in self.student_list:
            if i.name==modify_name:
                i.name=self.new_input(i.name,'请输出新修改的名字 回车则不再修改')
                i.age=self.new_input(i.age,"请输入新修改的年纪，回车后则不再修改")
                i.gender=self.new_input(i.gender,'请输入新修改的性别信息，回车后不再修改')
                break
        else:
            print("查无此人")
    #查找学生信息
    def search_student(self):
        search_name=input("输入要查找的学生姓名")
        for i in self.student_list:
            if i.name==search_name:
                print(f'姓名 {i.name},年龄 {i.age},性别 {i.gender}')
                break
        else:
            print("查无此人")
    # 查找全部学生的信息
    def show_student(self):
        for i in self.student_list:
            print(f'{i.name}\t\t{i.age}\t\t{i.gender}')
    # 保存学生信息
    def save_student(self):
        # 1.打开文件
        """2.1:学员对象转化成字典 用列表推导式
        2.2 文件写入 字符串"""
        new_list=[i.__dict__ for i in self.student_list]
        file_manager.write_file('students.txt',str(new_list))
        # 2。数据写入文件,
        # file.close()
    # 加载信息
    def load_student(self):
        try:
            file=open('/Users/wangmengmeng/numpy_pandas_matplotlib_practices/学生管理系统/data/students.txt', 'r')
        except FileNotFoundError:
            file=open('/Users/wangmengmeng/numpy_pandas_matplotlib_practices/学生管理系统/data/students.txt', 'w')
        else:
            # 读取数据
            data=file.read()
            # 2.文件中读取的数据都是字符串且字符串是字典数据，所以需要转换数据类型
            # 再转换字典为对象后，存储到学院列表
            new_list=eval(data)
            # 创建学生类
            self.student_list=[Student(i['name'],i['age'],i['gender']) for i in new_list]
        finally:
            pass
        file.close()

    # 重写input方法
    def new_input(self,old,new):
        input_str=input(new)
        if len(input_str)>0:
            return input_str
        else:
            return old


