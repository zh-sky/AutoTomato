from Util.write_user_command import WriteUserCommand
from Util.server import Server
from BasePy.base_driver import BaseDriver
from BasePy.tomato_case import ParameTestCase
from Case.login_case import LoginCase
from Case.room_status_case import RoomStatusCase
from Case.order_case import OrderCase
import HTMLTestRunner
import unittest
import multiprocessing


def appium_init():
    write_file = WriteUserCommand()
    write_file.clear_data()  # 清空操作先暂时放在这执行
    server = Server()
    server.main()


def get_suite(i):
    file_path = ('../report/' + 'case_one.html')
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'番茄来了测试报告', description=u'测试版的哦哦哦', verbosity=2)
        tomato_driver = get_driver(i)
        suite = unittest.TestSuite()
        suite.addTest(ParameTestCase.parametrize(LoginCase, driver=tomato_driver))
        suite.addTest(ParameTestCase.parametrize(RoomStatusCase, driver=tomato_driver))
        suite.addTest(ParameTestCase.parametrize(OrderCase, driver=tomato_driver))
        # suite.addTest(ParameTestCase.parametrize(FinanceCase, driver=driver))
        runner.run(suite)
    tomato_driver.quit()


def get_driver(i):
    """
    获取driver
    :param i:
    :return:
    """

    base_driver = BaseDriver()
    return base_driver.iOS_driver(i)


def get_count():
    write_file = WriteUserCommand()
    return write_file.get_lines()


if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_count()):
        # print(i)
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()


