import unittest
from Business.login_business import LoginBusiness
from Business.room_status_business import RoomStatusBusiness
from Business.order_business import OrderBusiness
from Business.finance_business import FinanceBusiness


class ParameTestCase(unittest.TestCase):
    driver = None

    def __init__(self, methodName='runTest', driver=None):
        super(ParameTestCase, self).__init__(methodName)
        ParameTestCase.driver = driver
        self.login_business = LoginBusiness(driver)
        self.room_status_business = RoomStatusBusiness(driver)
        self.order_business = OrderBusiness(driver)
        self.finance_business = FinanceBusiness(driver)

    @staticmethod
    def parametrize(testcase_class, driver=None):
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(testcase_class(name, driver=driver))
        return suite

    # @classmethod
    # def tearDownClass(cls):
    #     ParameTestCase.driver.quit()


