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
        self.screen_width = driver.get_window_size()['width']
        self.screen_height = driver.get_window_size()['height']
        self.get_by_element = GetByElement(self.driver)
        self.section = section

    def alert_allow(self):
        # allow 提示框
        self.driver.switch_to_alert()

    def get_back_button_element(self):
        """
        获取返回按钮元素
        :return:
        """
        return self.get_by_element.get_element('base_element', 'back_button')

    def get_toast_element(self, message):
        """
        获取toast 元素信息
        """
        time.sleep(2)
        toast_element = ('xpath', "//*[contains(@text, "+message+")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))

    # 向左边滑动
    def swipe_left(self, x1, y, x2):
        self.driver.swipe(x1*self.screen_width, y*self.screen_height, x2*self.screen_width, y*self.screen_height)

    #向右边滑动
    def swipe_right(self, x1, y, x2):
        self.driver.swipe(x1*self.screen_width, y*self.screen_height, x2*self.screen_width, y*self.screen_height)

    # 向上滑动
    def swipe_up(self, x, y1, y2):
        self.driver.swipe(x*self.screen_width, y1*self.screen_height, x*self.screen_width, y2*self.screen_height)

    # 向下滑动
    def swipe_bottom(self, x, y1, y2):
        self.driver.swipe(x*self.screen_width, y1*self.screen_height, x*self.screen_width, y2*self.screen_height)


