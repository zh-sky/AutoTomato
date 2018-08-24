from Handle.order_handle import OrderHandle


class OrderBusiness:
    def __init__(self, driver):
        self.order_handle = OrderHandle(driver, 'order_element')

    def check_expect_arrive_order(self):
        """
        查看预抵订单
        :return:
        """
        self.order_handle.click_order()
        self.order_handle.click_expect_arrive()
        if self.order_handle.find_cell():
            return True
        return False

    def check_expect_leave_order(self):
        """
        查看预离订单
        :return:
        """
        self.order_handle.click_order()
        self.order_handle.click_expect_leave()
        if self.order_handle.find_cell():
            return True
        return False

    def search_order(self, text):
        """
        输入框输入文字 搜索订单
        :param text: 文字
        :return:
        """
        self.order_handle.search_text(text)
        if self.order_handle.find_cell():
            return True
        return False

    def back_home(self):
        """
        返回首页
        :return:
        """
        self.order_handle.click_back_button()