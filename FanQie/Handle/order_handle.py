from Page.order_page import OrderPage


class OrderHandle:
    """
    所有订单页面的操作
    """
    def __init__(self, driver, section):
        self.order_page = OrderPage(driver, section)

    def click_order(self):
        """
        点击订单格子
        :return:
        """
        self.order_page.get_order_button_element().click()

    def click_expect_arrive(self):
        """
        点击预抵
        :return:
        """
        self.order_page.get_expect_arrive_element().click()

    def click_expect_leave(self):
        """
        点击预离
        :return:
        """
        self.order_page.get_expect_leave_element().click()

    def search_text(self, text):
        """
        搜索框输入文字 搜索订单
        :param text:
        :return:
        """
        self.order_page.get_search_element().send_keys(text)

    def click_back_button(self):
        """
        点击返回
        :return:
        """
        self.order_page.get_back_button_element()[0].click()

    def find_cell(self):
        """
        检查相应内容是否出现
        :return:
        """
        cell_flag = self.order_page.get_cell_element()
        if cell_flag:
            return True
        return False
