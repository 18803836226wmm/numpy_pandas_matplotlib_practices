import configparser
# import project_path
class ReadConfig:
    """方法一"""
    @staticmethod
    def get_config(file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')
        return cf[section][option]
if __name__ == '__main__':
    file= '/python操作excel+txt+csv文件/接口测试excel/case.config'
    res=eval(ReadConfig.get_config(file,'MODE','mode'))
    print(res)

    print(type(res))