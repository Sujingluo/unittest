# coding = utf-8

import unittest
import requests


class InterfaceTestCase(unittest.TestCase):

    # 第一个执行,灵活切换环境
    def setUp(self):
        self.domain = "http://localhost:12306"

    # 最后一个执行
    def tearDown(self):
        print('after')

    # 验证posts中json数据的第一个数据和最后一个数据
    def test_1_get_all_posts(self):
        print('test get_all_posts')
        url = self.domain + '/posts'
        result = requests.get(url).json()

        self.assertEqual(len(result), 3)

        self.assertEqual(result[0]['title'], 'first post')
        self.assertEqual(result[0]['url'], '/posts/1')

        self.assertEqual(result[-1]['title'], 'how to learn interface test')
        self.assertEqual(result[-1]['url'], '/posts/3')

    # 验证post/1下的数据
    def test_2_get_first_posts(self):
        print('test get_first_posts')
        url = self.domain + '/posts/1'
        result = requests.get(url).json()

        self.assertEqual(result[0]['title'], 'first post')
        self.assertEqual(result[0]['content'], 'this is first post')

    # 跳过某个case
    @unittest.skip("I don't want to run this case.")
    def test_3_skip_posts(self):
        print('test_skip_posts')




    # 方便切换环境
    # def url(self, path):
    #     return self.domain + path


if __name__ == '__main__':
    unittest.main()


