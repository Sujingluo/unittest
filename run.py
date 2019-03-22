# coding = utf-8

import unittest
import HTMLTestRunner

from test_case import test_mock
from test_case.test_mock import InterfaceTestCase

from BeautifulReport import BeautifulReport
import test_case

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [InterfaceTestCase('test_2_get_first_posts'), InterfaceTestCase('test_1_get_all_posts')]
    suite.addTests(tests)

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(InterfaceTestCase))
    #
    # with open('UnittestTextReport.txt') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(suite)

    # suite = unittest.defaultTestLoader.discover('test_case', pattern='test_mock.py', top_level_dir=None)
    # # runner = unittest.TextTestRunner()
    # result = BeautifulReport(suite)
    # result.report(filename='report', description='testReport', log_path='test_report')
    # # # runner.run(suite)
    # # BeautifulReport(suite).report(filename='report', description='testReport', log_path='test_report')

    report_path = "C:\\Users\\zsxia\\PycharmProjects\\TestDemo\\unittest_demo\\test_report\\reult.html"

    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='unit test',
        description='This demonstrates the report output by HTMLTestRunner.'
    )
    runner.run(suite)

    EXPECTED = u""

    fp.close()

