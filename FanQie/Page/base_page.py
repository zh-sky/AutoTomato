from Util.get_by_element import GetByElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, driver, section):
        """
        构造函数
        :param driver: 启动的服务
        :param section: yaml 文件中对应的section
        """
        self.driver = driver
        self.get_by_element = GetByElement(self.driver)
        self.section = section

    def alert_allow(self):
        # allow 提示框
        self.driver.switch_to_alert()

    def get_toast_element(self, message):
        """
        获取toast 元素信息
        """
        time.sleep(2)
        toast_element = ('xpath', "//*[contains(@text, "+message+")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))
