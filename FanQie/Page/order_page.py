from Page.base_page import BasePage


class OrderPage(BasePage):
    def get_order_button_element(self):
        """
        获取订单元素信息
        :return:
        """
        return self.get_by_element.get_element(self.section, 'orders')

    def get_expect_arrive_element(self):
        """
        获取预抵的元素信息
        :return:
        """
        return self.get_by_element.get_element(self.section, 'expected_arrive')

    def get_expect_leave_element(self):
        """
        获取鱼离得元素信息
        :return:
        """
        return self.get_by_element.get_element(self.section, 'expected_leave')

    def get_search_element(self):
        """
        获取搜索框元素
        :return:
        """
        return self.get_by_element.get_element(self.section, 'search_bar')

    def get_cell_element(self):
        """
        获取cell元素
        :return:
        """
        return self.get_by_element.get_element(self.section, 'cell')