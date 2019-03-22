# coding = utf-8

import unittest

class TestMathFunc(unittest.TestCase):

    def setUp(self):
        print("运行testcase之前执行")

    def tearDown(self):
        print("运行testcare之后执行")

    # def test_01(self):
    #     self.assertEqual(3, add(1, 2))