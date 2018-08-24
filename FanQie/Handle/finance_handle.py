from Page.finance_page import FinancePage


class FinanceHandle:
    """
    财务页面的所有操作
    """
    def __init__(self, driver, section):
        self.finance_page = FinancePage(driver, section)

    def click_finance_button(self):
        """
        点击财务格子
        :return:
        """
        self.finance_page.get_finance_element().click()

    def click_start_date_button(self):
        """
        点击财务页面的起始时间
        :return:
        """
        self.finance_page.get_start_date_element().click()

    def click_end_date_button(self):
        """
        点击财务页面的结束时间
        :return:
        """
        self.finance_page.get_end_date_element().click()

    def click_remember_button(self):
        """
        点击  "记一笔"
        :return:
        """
        self.finance_page.get_remember_element().click()

    def click_confirm_date_button(self):
        """
        点击日历控件上的确认按钮
        :return:
        """
        self.finance_page.get_confirm_date_element()[0].click()

    def send_num_textfield(self, text):
        """
        填写商品数量
        :param text: 数量
        :return:
        """
        self.finance_page.get_num_element()[0].send_keys(text)

    def send_price_textfield(self, text):
        """
        填写商品单价
        :param text: 单价
        :return:
        """
        self.finance_page.get_price_element()[0].send_keys(text)

    def send_money_textfield(self, text):
        """
        填写支出/收入 金额
        :param text:金额
        :return:
        """
        self.finance_page.get_money_element()[0].send_keys(text)

    def click_good_sale(self):
        """
        点击商品销售
        :return:
        """
        self.finance_page.get_sale_element()[0].click()

    def click_cost_expend(self):
        """
        点击费用支出
        :return:
        """
        self.finance_page.get_cost_element()[0].click()

    def click_other_income(self):
        """
        点击其他收入
        :return:
        """
        self.finance_page.get_other_element()[0].click()

    def click_save_button(self):
        """
        点击保存按钮
        :return:
        """
        self.finance_page.get_save_element().clcik()

    def click_back_button(self):
        """
        点击返回按钮
        :return:
        """
        self.finance_page.get_back_button_element()[0].clcik()

    def get_result_toast(self, message):
        """
        获取toast信息
        :param message: 信息
        :return:
        """
        if self.finance_page.get_toast_element(message):
            return True
        return False

    def swipe_up(self, x, y1, y2):
        """
        向上滑动
        :return:
        """
        self.finance_page.swipe_up(x, y1, y2)