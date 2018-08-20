from Handle.finance_handle import FinanceHandle


class FinanceBusiness:
    def __init__(self, driver):
        self.finance_handle = FinanceHandle(driver, 'finance_element')

    def chose_start_date(self):
        """
        选择开始时间
        :return:
        """
        self.finance_handle.click_finance_button()
        self.finance_handle.click_start_date_button()
        self.finance_handle.finance_page.swipe_up(0.2, 0.9, 0.85)
        self.finance_handle.click_confirm_date_button()

    def chose_end_date(self):
        """
        选择结束时间
        :return:
        """
        self.finance_handle.click_end_date_button()
        self.finance_handle.finance_page.swipe_up(0.2, 0.9, 0.8)
        self.finance_handle.click_confirm_date_button()

    def remember_good_sale(self):
        """
        记一笔商品销售
        :return:
        """
        self.finance_handle.click_remember_button()
        self.finance_handle.send_num_textfield('2')
        self.finance_handle.send_price_textfield('3')
        self.finance_handle.click_save_button()
        if self.finance_handle.get_result_toast('保存成功'):
            return True
        return False

    def remember_money_cost(self):
        """
        记一笔费用支出
        :return:
        """
        self.finance_handle.click_remember_button()
        self.finance_handle.click_cost_expend()
        self.finance_handle.send_money_textfield('20')
        self.finance_handle.click_save_button()
        if self.finance_handle.get_result_toast('保存成功'):
            return True
        return False

    def remember_other_income(self):
        """
        记一笔其他收入
        :return:
        """
        self.finance_handle.click_remember_button()
        self.finance_handle.click_other_income()
        self.finance_handle.send_money_textfield('30')
        self.finance_handle.click_save_button()
        if self.finance_handle.get_result_toast('保存成功')
            return True
        return False

    def back_home(self):
        """
        返回主页
        :return:
        """
        self.finance_handle.click_back_button()