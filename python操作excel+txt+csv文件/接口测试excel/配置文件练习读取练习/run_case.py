import unittest
'from test.test_666 import test_unittest'
#单个用例加载
suite=unittest.TestCase()
case1='test_unittest("test_b")'
case2='test_unittest("test_a")'
suite.addTest(case1)
suite.addTest(case2)
