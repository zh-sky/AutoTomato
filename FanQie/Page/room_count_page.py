from Page.base_page import BasePage


class RoomCountPage(BasePage):

    def get_room_num_element(self):
        """
        获取单个房间数量元素
        :return:
        """
        return self.get_by_element.get_element(self.section, 'room_count')

    def get_batch_element(self):
        """
        获取批量按钮元素
        :return:
        """
        return self.get_by_element.get_element(self.section, '')
