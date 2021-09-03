"""
1.读取小文件
"""
def read_small_txt():
    """1。读取小文件"""
    file_name='small_txt.txt'
    with open(file_name,'r',encoding='utf-8') as f:
        print(f.read())
"""
2。按行读取大文件
"""
def read_large_txt():
    """按行读取文件"""
    file_name='large_txt.txt'
    # with open(file,'r',encoding='utf-8') as f: # 不能用这个来读取txt文件
    file=open(file_name,'r',encoding='utf-8')
    # print(file.read())
    for line in file:
        line=line.rstrip('\n')
        if isinstance(line,str) and line !='':
            print(line)
    file.close()
"""3.写文件"""
def write_txt():
    """写文件"""
    with open('small_txt.txt','w',encoding='utf-8') as f:
        f.write('我来自何方，我情归何处'+'\n')
"""追加写入文件"""
def write_add_txt():
    with open('small_txt.txt','a+',encoding='utf-8') as f:
        f.write('谁在下一刻呼唤我')
if __name__ == '__main__':
    read_small_txt()
    read_large_txt()
    # write_txt()
    write_add_txt()