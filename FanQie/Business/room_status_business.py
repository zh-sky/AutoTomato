from Handle.room_status_handle import RoomStatusHandle
import time

class RoomStatusBusiness:
    """
    获取房态页面的所有业务
    """
    def __init__(self, driver):
        self.room_status_handle = RoomStatusHandle(driver, 'room_status_element')

    def check_in_room(self):
        """
        入住房间
        选择房间 -> 点击入住按钮 -> 输入联系人姓名和手机号 -> 完成 ->房态页面显示入住的房间
        :return:
        """
        self.room_status_handle.click_room_status()
        time.sleep(2)
        self.room_status_handle.click_room_button(65)
        time.sleep(1)
        self.room_status_handle.click_checkin_button()
        self.room_status_handle.send_contact_username('测试入住')
        self.room_status_handle.send_contact_phone('132333335555')
        self.room_status_handle.click_done_button()
        if self.room_status_handle.get_result_toast('房间入住成功'):
            return True
        return False

    def reserve_room(self):
        """
        预定房间
        选择房间 -> 点击预定按钮 -> 输入联系人姓名和手机号 -> 完成 ->房态页面显示预定成功的房间
        :return:
        """
        time.sleep(2)
        self.room_status_handle.click_room_button(82)
        self.room_status_handle.click_reserve_button()
        self.room_status_handle.send_contact_username('测试预定')
        self.room_status_handle.send_contact_phone('132333335555')
        self.room_status_handle.click_done_button()
        if self.room_status_handle.get_result_toast('房间预订成功'):
            return True
        return False

    def back_home(self):
        """
        返回主页
        :return:
        """
        self.room_status_handle.click_back_button()
