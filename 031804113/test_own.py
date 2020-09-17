import unittest
import encapsulation
from BeautifulReport import BeautifulReport

class TEST_turntin(unittest.TestCase):


    def test(self):
        print("start..")
        print("测试文本为test.txt")
        encapsulation.solveok('test.txt', 'test.txt', 'ans.txt')

    def test9(self):
        print("测试文本为test9.txt")
        encapsulation.solveok('test.txt','test9.txt','ans.txt')

    def test8(self):
        print("测试文本为test8.txt")
        encapsulation.solveok('test.txt', 'test8.txt', 'ans.txt')

    def test7(self):
        print("测试文本为test7.txt")
        encapsulation.solveok('test.txt', 'test7.txt', 'ans.txt')

    def test6(self):
        print("测试文本为test6.txt")
        encapsulation.solveok('test.txt', 'test6.txt', 'ans.txt')
    def test1(self):
        print("测试文本为test1.txt")
        encapsulation.solveok('test.txt', 'test1.txt', 'ans.txt')

    def test2(self):
        print("测试文本为test2.txt")
        encapsulation.solveok('test.txt', 'test2.txt', 'ans.txt')

    def test3(self):
        print("测试文本为test3.txt")
        encapsulation.solveok('test.txt', 'test3.txt', 'ans.txt')

    def test4(self):
        print("测试文本为test4.txt")
        encapsulation.solveok('test.txt', 'test4.txt', 'ans.txt')

    def test5(self):
        print("测试文本为test5.txt")
        encapsulation.solveok('test.txt', 'test5.txt', 'ans.txt')
        print("Finally!!!")

if __name__ == '__main__':
    print("let's beginning")
    suite = unittest.TestSuite()
    suite.addTest(TEST_turntin('test'))
    suite.addTest(TEST_turntin('test9'))
    suite.addTest(TEST_turntin('test8'))
    suite.addTest(TEST_turntin('test7'))
    suite.addTest(TEST_turntin('test6'))
    suite.addTest(TEST_turntin('test1'))
    suite.addTest(TEST_turntin('test2'))
    suite.addTest(TEST_turntin('test3'))
    suite.addTest(TEST_turntin('test4'))
    suite.addTest(TEST_turntin('test5'))
    runner = BeautifulReport(suite)
    runner.report(
        description='论文(own)查重报告',
        filename='finally_own.html',
        log_path='C:/Users/guoch/Desktop/sim_0.8'
    )
