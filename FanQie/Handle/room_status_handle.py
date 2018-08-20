from Page.room_status_page import RoomStatusPage


class RoomStatusHandle:
    """
    房态页面的所有操作
    """
    def __init__(self, driver, section):
        self.room_status_page = RoomStatusPage(driver, section)

    def click_room_status(self):
        """
        首页点击房态格子
        :return:
        """
        self.room_status_page.get_room_status_element().click()

    def click_room_button(self, num):
        """
        点击房间按钮
        :return:
        """
        self.room_status_page.get_room_button_element(num).click()

    def click_checkin_button(self):
        """
        点击入住按钮
        :return:
        """
        self.room_status_page.get_room_checkin_element().click()

    def click_reserve_button(self):
        """
        点击预定按钮
        :return:
        """
        self.room_status_page.get_room_order_element().click()

    def send_contact_username(self, username):
        """
        输入联系人姓名
        :return:
        """
        self.room_status_page.get_contact_user_element().send_keys(username)

    def send_contact_phone(self, phone):
        """
        输入联系人手机号
        :param phone:
        :return:
        """
        self.room_status_page.get_contact_phone_element().send_keys(phone)

    def click_done_button(self):
        """
        点击完成按钮
        :return:
        """
        self.room_status_page.get_done_element().click()

    def click_back_button(self):
        """
        点击返回按钮
        :return:
        """
        self.room_status_page.get_back_button_element().click()

    def get_result_toast(self, message):
        """
        获取操作结果toast
        :return:
        """
        toast_element = self.room_status_page.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False
