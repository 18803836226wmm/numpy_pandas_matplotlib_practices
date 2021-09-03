import json
"""
json.dumps():将python对象编码成json字符串
json.loads():将json字符串解码成python对象
json.dump():将python中的对象转化成json储存到文件中
json.load():将文件中的json的格式化转化成python对象提取
"""
with open('./data/test.json') as f:
    a=json.load(f)
print(a)
dict={
    "name":"狂龙",
    "age":20,
    "phone":"123"
}
with open('./data/test.json','a+') as pp:
    # ensure_ascii=True：默认输出ASCLL码，如果把这个该成False,就可以输出中文
    json.dump(dict,pp,ensure_ascii=False)