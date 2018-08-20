from Page.base_page import BasePage


class FinancePage(BasePage):
    def get_finance_element(self):
        """
        获取财务元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'finance')

    def get_start_date_element(self):
        """
        获取起始时间元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'start_date')

    def get_end_date_element(self):
        """
        获取结束时间元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'end_date')

    def get_cancel_date_element(self):
        """
        获取日期控件上的取消按钮元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'cancel_date')

    def get_confirm_date_element(self):
        """
        获取日期控件上的确认按钮元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'confirm_date')

    def get_picker_element(self):
        """
        获取日期控件元素
        :return:
        """
        return self.get_by_element.get_element(self.section, 'picker_view')

    def get_remember_element(self):
        """
        获取记一笔元素
        :return:
        """
        return self.get_by_element.get_element(self.section, 'id_记一笔')

    def get_num_element(self):
        """
        获取商品数量元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'num')

    def get_price_element(self):
        """
        获取商品单价元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'single_price')

    def get_money_element(self):
        """
        获取金额元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'money_num')

    def get_sale_element(self):
        """
        获取商品销售元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'goods_sale')

    def get_cost_element(self):
        """
        获取费用支出元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'cost_expend')

    def get_other_element(self):
        """
        获取其他收入元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'other_income')

    def get_save_element(self):
        """
        获取保存按钮元素
        :return:
        """
        self.get_by_element.get_element(self.section, 'save_button')