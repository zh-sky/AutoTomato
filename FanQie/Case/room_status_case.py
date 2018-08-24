import BasePy


class RoomStatusCase(BasePy.ParameTestCase):

    def test_a_room_checkIn(self):
        """
        测试房态页面 入住房间
        :return:
        """
        checkIn_flag = self.room_status_business.check_in_room()
        self.assertTrue(checkIn_flag, '房间入住失败')

    # @BasePy.my_skip
    def test_b_room_order(self):
        """
        测试房态页面 预定房间
        :return:
        """
        reserve_flag = self.room_status_business.reserve_room()
        self.assertTrue(reserve_flag, '房间预订失败')

    # @BasePy.my_skip
    def test_c_back(self):
        """
        返回主页面
        """
        self.room_status_business.back_home()
