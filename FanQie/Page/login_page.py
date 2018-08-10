from BaseDriver.base_driver import BaseDriver
from Util.get_by_element import GetByElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    """
    获取登录页面所有页面元素的信息
    """
    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.iOS_driver(i)
        self.get_by_element = GetByElement(self.driver)
        self.section = 'login_element'

    def login_allow(self):
        # allow 提示框
        self.driver.switch_to_alert()

    def get_username_element(self):
        """
        获取用户名信息
        """
        return self.get_by_element.get_element('username')

    def get_password_element(self):
        """
        获取密码框信息
        """
        return self.get_by_element.get_element('password')

    def get_login_button_element(self):
        """
        获取登录按钮元素信息
        """
        return self.get_by_element.get_element('login_button')

    def get_toast_element(self, message):
        """
        获取toast 元素信息
        """
        time.sleep(2)
        toast_element = ('xpath', "//*[contains(@text, "+message+")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))
