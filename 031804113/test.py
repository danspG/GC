import unittest
import encapsulation
from BeautifulReport import BeautifulReport

class TEST_turntin(unittest.TestCase):

    def orig_self(self):
        print("测试文本为orig.txt")
        encapsulation.solveok('orig.txt', 'orig.txt', 'ans.txt')

    def orig_add(self):
        print("测试文本为orig_0.8_add.txt")
        encapsulation.solveok('orig.txt','orig_0.8_add.txt','ans.txt')

    def orig_del(self):
        print("测试文本为orig_0.8_del.txt")
        encapsulation.solveok('orig.txt', 'orig_0.8_del.txt', 'ans.txt')

    def orig_dis_1(self):
        print("测试文本为orig_0.8_dis_1.txt")
        encapsulation.solveok('orig.txt', 'orig_0.8_dis_1.txt', 'ans.txt')

    def orig_dis_3(self):
        print("测试文本为orig_0.8_dis_3.txt")
        encapsulation.solveok('orig.txt', 'orig_0.8_dis_3.txt', 'ans.txt')
    def orig_dis_7(self):
        print("测试文本为orig_0.8_dis_7.txt")
        encapsulation.solveok('orig.txt', 'orig_0.8_dis_7.txt', 'ans.txt')

    def orig_dis_10(self):
        print("测试文本为orig_0.8_dis_10.txt")
        encapsulation.solveok('orig.txt', 'orig_0.8_dis_10.txt', 'ans.txt')

    def orig_dis_15(self):
        print("测试文本为orig_0.8_dis_15.txt")
        encapsulation.solveok('orig.txt', 'orig_0.8_dis_15.txt', 'ans.txt')

    def orig_mix(self):
        print("测试文本为orig_0.8_mix.txt")
        encapsulation.solveok('orig.txt', 'orig_0.8_mix.txt', 'ans.txt')

    def orig_rep(self):
        print("测试文本为orig_0.8_rep.txt")
        encapsulation.solveok('orig.txt', 'orig_0.8_rep.txt', 'ans.txt')
        print("Finally!!!")

if __name__ == '__main__':
    print("let's beginning")
    suite = unittest.TestSuite()
    suite.addTest(TEST_turntin('orig_self'))
    suite.addTest(TEST_turntin('orig_add'))
    suite.addTest(TEST_turntin('orig_del'))
    suite.addTest(TEST_turntin('orig_dis_1'))
    suite.addTest(TEST_turntin('orig_dis_3'))
    suite.addTest(TEST_turntin('orig_dis_7'))
    suite.addTest(TEST_turntin('orig_dis_10'))
    suite.addTest(TEST_turntin('orig_dis_15'))
    suite.addTest(TEST_turntin('orig_mix'))
    suite.addTest(TEST_turntin('orig_rep'))
    runner = BeautifulReport(suite)
    runner.report(
        description='论文查重报告',
        filename='finally.html',
        log_path='C:/Users/guoch/Desktop/软工实践'
    )
