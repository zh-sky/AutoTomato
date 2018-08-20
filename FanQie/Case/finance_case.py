from Case.tomato_case import ParameTestCase


class FinanceCase(ParameTestCase):

    def test_a__date(self):
        """
        测试财务页面不同时间间隔内的收支
        :return:
        """
        self.finance_business.chose_start_date()
        self.finance_business.chose_end_date()

    def test_b_remember_good_sale(self):
        """
        测试记账->商品销售
        :return:
        """
        self.assertTrue(self.finance_business.remember_good_sale(), '商品销售记账失败')

    def test_c_remember_cost(self):
        """
        测试记账->费用支出
        :return:
        """
        self.assertTrue(self.finance_business.remember_money_cost(), '费用支出记账失败')

    def test_d_remember_other_income(self):
        """
        测试记账->其他收入
        :return:
        """
        self.assertTrue(self.finance_business.remember_other_income(), '其他收入记账失败')
