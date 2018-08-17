from Page.base_page import BasePage


class RoomStatusPage(BasePage):

    def get_room_status_element(self):
        """
        获取房态格子元素
        :return:
        """
        print(self.get_by_element.get_element(self.section, 'room_status'))
        return self.get_by_element.get_element(self.section, 'room_status')

    def get_room_button_element(self, num):
        """
        获取房态页面单个房间元素 单个房间没有唯一标识 拿到所有房间色数组 取其中一个
        num:哪个房间
        :return:
        """
        room_button_elements = self.get_by_element.get_element(self.section, 'room_button')
        return room_button_elements[num]

    def get_room_checkin_element(self):
        """
        获取入住房间按钮
        :return:
        """
        return self.get_by_element.get_element(self.section, 'check_in')

    def get_room_order_element(self):
        """
        获取预定房间的按钮
        :return:
        """
        return self.get_by_element.get_element(self.section, 'reserve')

    def get_contact_user_element(self):
        """
        获取联系人姓名输入框
        :return:
        """
        return self.get_by_element.get_element(self.section, 'contact_name')

    def get_contact_phone_element(self):
        """
        获取联系人手机号输入框
        :return:
        """
        return self.get_by_element.get_element(self.section, 'contact_phone')

    def get_done_element(self):
        """
        获取完成按钮
        :return:
        """
        return self.get_by_element.get_element(self.section, 'done')

    def get_back_element(self):
        """
        获取返回按钮
        :return:
        """
        return self.get_by_element.get_element(self.section, 'back_button')
