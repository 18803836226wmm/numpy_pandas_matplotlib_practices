"""
yaml：是另外一种标记芋圆，yaml是专门用来写配置文件的语言，非常简洁和强大，之前用ini也可以写文件，但是看了yaml后，发现这个更直观 更方便
有点类似与json格式
1。yaml语法规则：
    大小写敏感
    使用缩进表示层级关系
    缩进时不允许使用tab键盘，只要相同层级的元素左侧对齐即可
    # 星号表示注释 从这个字符 一直到行尾
2。yaml支持的数据结构有3种
    对象：键值对的集合，又称为映射 哈希 字典
    数组：一组按次序排列的值，称为序列 列表
    纯量：单个的 不可再分的值，字符串、布尔值、整数、浮点数、null 时间 日期
3。数据格式一
    yaml:格式的数据展示样式
name:john smith
age:37
spouse:
    name:jane smith
    age:25
children:
    - name:jimmy smith
      age:15
    - name:jenny smith
      age:12
和它对应的json文件
{name:"john smith",
age:37,
spouse:{name:"jimmy smith",age:25},
children:[{name:"jimmy smith",age:15},
        {name:"jimmy smith",age:12}]
}
"""


