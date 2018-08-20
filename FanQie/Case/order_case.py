from Case.tomato_case import ParameTestCase


class OrderCase(ParameTestCase):
    def test_a_expected_arrive(self):
        """
        测试预抵订单显示
        :return:
        """
        self.assertTrue(self.order_business.check_expect_arrive_order(), '预抵订单数据有误')

    def test_b_expected_leave(self):
        """
        测试预离订单显示
        :return:
        """
        self.assertTrue(self.order_business.check_expect_leave_order(), '预离订单数据有误')

    def test_c_back(self):
        """
        测试搜索订单功能
        :return:
        """
        self.assertTrue(self.order_business.search_order('测试入住'), '搜索订单失败')

    def test_d_back(self):
        """
        返回首页
        :return:
        """
        self.order_business.back_home()
