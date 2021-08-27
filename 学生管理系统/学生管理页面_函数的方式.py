"""
要求：1。添加学生
    2。删除学生
    3。修改学生
    4。查询学生
    5。遍历学生信息
    6。退出系统
写法：
1。先考虑整体的框架
2。提示用户选择功能
3。获取用户选择功能
4。根据用户选择执行相应的操作
"""
# 0学生管理系统页面
def showInfo():
    print("-" * 30)
    print(" 学生管理系统 v1.0")
    print(" 1:添加学生的信息")
    print(" 2:删除学生的信息")
    print(" 3:修改的信息")
    print(" 4:查询学生的信息")
    print(" 5:遍历学生的信息")
    print(" 6:退出系统")
    print("-" * 30)
#添加学生信息
def addStudent(studentsTemp):
    name=input("请输入姓名")
    stuid=input("请输入学号")
    age=input("请输入年龄")
# 判断是否添加这个学生，如果学生姓名已存在报错提示；不存在就添加成功
    global students
    # 不允许学号重复 判断输入的学号与列表中的id是否相等
    for i in  students:
        if stuid==i['id']:
            # return函数的作用是退出当前函数，后面添加信息的代码不执行
            return
    #如果不存在，添加数据，准备空字典，字典新增数据，列表追加字典
    stuinfo={}
    stuinfo['name']=name
    stuinfo['stuid']=stuid
    stuinfo['age']=age
    studentsTemp.append(stuinfo)
def del_info():
    #用户输入删除的学生学号，并且判断是否存在
    del_name=input("请输入要删除的姓名")
    global students
    for i in students:
        if del_name==i['name']:
            students.remove(i)
            break
        else:
            print("该学生不存在")
    print(students)
def modity_info():
    #输入想要修改的学生姓名
    modity_name=input('输入要修改的学生姓名')
    # 判断是否存在，存在就修改，不存在提示
    global students
    for i in students:
        if modity_name==i['name']:
            i['id']=input('输入新学号')
            break
        else:
            print('学生不存在')
def print_all():
    #遍历所有学生信息
    for i in students:
        print(f"{i['id']}\t{i['name']}\t{i['age']}")
students=[]
while True:
    showInfo()
    key=int(input('输入选择的功能序号'))
    if key==1:
        addStudent(students)
    elif key==2:
        del_info()
    elif key==3:
        modity_info()
    elif key==6:
        exit_flag=input("确定要退出吗？ yes/no")
        if exit_flag=='yes':
            break
    else:
        print("输入有误")

