"""
unitest：单元测试框架是和python语言一套标准模块，封装提供了诸多操作测试用例和用例加载、测试前置、场景恢复以及测试结果输出等一系列类
和方法
1。unitest框架中四个核心组件
    testcase：测试用例类，编写测试用例脚本时需要继承该类，从而具有该类的属性和方法，一个testcase实例就是一个测试用例，其中测试用例
    方法都以test开头
    testsuite：测试集，也就是测试用例的集合 用来组织用例
    testrunner：用来执行测试用例，并且返回测试用例执行结果。可以用图形或者文本将测试结果形象的展示出来，htmltestrunner 用来生成
    图形化报告
    testfixture：测试夹件 主要用于测试用例的前置初始化和执行后的销毁
2.unitest.TestSuite()提供单个用例加载的方法
addTest（）：单个用例加载，当然也可以将多个用例的方法名放入到addTest()中 加载多条测试用例
loadTestFromTestCase(测试类名)：添加一个测试类
loadTestFromModule(模块名称)：添加一个模块
testrunner：测试运行
testrunner:就是用来执行测试用例的，并且可以生成相应的测试报告，报告有两种形式 一个是text 一个是html

3。ddt：
    什么是ddt，测试步骤相同，代码一样，测数据不同，当我们输入一组测试数据的时候，测试框架会自动生成独立的多个测试用例的方法就是ddt
    但是ddt不等于是数据驱动 数据驱动只是实现了数据驱动的思想
    实际框架中测试数据不一定是放在代码里，代码要做数据分离，实际是爸数据放在excel、yaml或者json中，等等，作者实际框架中最多用这3个
"""
import unittest
import ddt
data=[(1,2,3),(1,3,4),(1,4,5)]
# testcase 主要后续用于识别测试用例文件编写测试用例的类，必须继承unittest.TestCase作为测试类
# ddt 装饰类，也就是继承自TestCase的类，可以理解为这个类戴上一个帽子
@ddt.ddt
class test_unitest(unittest.TestCase):
    # 装饰测试方法，参数是一系列的值
    # 注意要加上*号 多组数据。@ddt.data(*data)相当于@ddt.data((1,2,3),(1,3,4))
    #每次运行都会从data中取出一组数据，动态生成一个独立的测试用例方法
    @ddt.data(*data)
    def testAdd(self, test_data):
        print(test_data)
        self.assertEqual((test_data[0] + test_data[1]), test_data[2])
    """装饰参数方法，参数是文件名，文件可以是json或者yaml类型
        如果文件以.yml、.yaml结尾，ddt会作为yaml类型处理，其他文件作会作为json文件处理
        """
    @ddt.file_data('d1.json')
    def test_practices(self,first,second,value):
        self.assertEqual((first+second),value)
    @ddt.data([3,2,1],[5,3,2],[10,4,6])
    @ddt.unpack
    def test_oo(self,a,b,c):
        actual = int(a) - int(b)
        expected = int(c)
        self.assertEqual(actual, expected)

    def setUp(self):
        print('测试环境初始化执行setup')
    def tearDown(self):
        print("测试执行完成，运行teardown")
    def test_a(self):
        print("开始执行a测试用例a")
    def test_b(self):
        print("开始执行测试b")

if __name__ == '__main__':
    unittest.main()
