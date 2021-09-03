import os
project=os.path.split('')

#测试用例路径
test_case_path=os.path.join(project,"test_data",'mm.xlsx')
#测试报告
test_report_path=os.path.join(project,"resoult",'test.html')
# 配置文件读取路径读取当前要执行的测试用例
case_confg_path=os.path.join(project,"do_config",'case.config')