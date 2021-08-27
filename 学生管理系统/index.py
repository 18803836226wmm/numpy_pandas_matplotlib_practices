"""
程序的入口文件
退出方式：
    return：退出当前函数（方法），如果有返回值就接上相应的值，如果没有返回值，返回类型就是void 只写return
    break：把循环推出，退出所在的循环或者switch结构，也只是会跳一层，要注意
    continue:的功能类似break，但是他在退出后会继续下一次的循环，跳出本次循环，继续下一次的循环
"""
import sys
from 学生管理系统 import file_manager
from 学生管理系统 import model
from 学生管理系统 import tool
from 学生管理系统 import managerSystem
def register():
    #读取文件，查看文件里是否有数据，如果文件不存在，默认是一个字典
    data=file_manager.read_json('data.json',{})
    while True:
        teacher_name=input("请输入账号2-6位")
        if not 2<=len(teacher_name)<=6:
            print("账号不符合要求，重新输入")
        else:
            break
    if teacher_name in data:
        print("注册失败，账号已经被注册")
        return
    while True:
        password=input('请输入密码6-12位')
        if not 6<=len(password)<=12:
            print("密码不符合要求，请重新输入")
        else:
            break
    #用户名称、密码都已经输入，接下来将用户名、密码以key：value的形式存储
    # 可以创建一个teacher对象
    t=model.Teacher(teacher_name,password)
    data[t.name]=t.password
    file_manager.write_json('data.json',data)
def login():
    #读取文件，查看是否有数据，如果文件不存在，默认是一个字典
    data=file_manager.read_json('data.json',{})
    teacher_name=input("请输入老师的账号")
    if teacher_name not in data:
        print("登陆失败，账号没有注册")
        return
    password=input('请输入密码')
    if data[teacher_name]==tool.encrypt_password(password):
        managerSystem.name=teacher_name
        print('登陆成功')
        """当前是不理解这个操作的含义是什么？？？"""
        # 这个是teacher登陆成功的的时候，不是可以操作学生的信息吗？处理学生的信息，所以要调用学生类，且执行学生类中的run方法
        student_manager=managerSystem.StudentManager()
        student_manager.run()

    else:
        print("密码输入错误")
def start():
    content=file_manager.read_file('welcome.txt')
    while True:
        opertion=input(content+'\n请选择1-3')
        if opertion=='1':
            print("登陆")
            login()
        elif opertion=='2':
            print("注册")
            register()
        elif opertion=='3':
            print('退出')
            sys.exit()
        else:
            print('输入有误')
# 2。启动管理系统
if __name__ == '__main__':
    start()

