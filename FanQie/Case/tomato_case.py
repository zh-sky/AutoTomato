import unittest
import time
import sys
import HTMLTestRunner
from Business.login_business import LoginBusiness
from Util.server import Server
from Util.write_user_command import WriteUserCommand
import multiprocessing
sys.path.append('/Users/mike/picture')


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class TomatoCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print('this is setUpClass')
        cls.login_business = LoginBusiness(parames)

    def setUp(self):
        print('this is set up')

    def test01(self):
        self.login_business.login_pass()

    def test02(self):
        self.login_business.login_user_error()

    def tearDown(self):
        time.sleep(1)
        if sys.exc_info()[0]:
            self.login_business.login_handle.login_page.driver.save_screenshot('../jpg/test02.png')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)


def appium_init():
    write_file = WriteUserCommand()
    write_file.clear_data()  # 清空操作先暂时放在这执行
    server = Server()
    server.main()


def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(TomatoCase('test02', parame=i))
    # suite.addTest(TomatoCase('test01', parame=i))

    html_file = "../report/report" + str(i) + ".html"
    with open(html_file, 'wb') as fr:
        HTMLTestRunner.HTMLTestRunner(stream=fr).run(suite)


def get_count():
    write_file = WriteUserCommand()
    return write_file.get_lines()


if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_count()):
        print(i)
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
