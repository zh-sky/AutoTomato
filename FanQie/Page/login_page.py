from Page.base_page import BasePage


class LoginPage(BasePage):
    """
    获取登录页面所有页面元素的信息
    """

    def get_username_element(self):
        """
        获取用户名信息
        """
        return self.get_by_element.get_element(self.section, 'username')

    def get_password_element(self):
        """
        获取密码框信息
        """
        return self.get_by_element.get_element(self.section, 'password')

    def get_login_button_element(self):
        """
        获取登录按钮元素信息
        """
        return self.get_by_element.get_element(self.section, 'login_button')

    def get_content_page_status_element(self):
        """
        登录成功后获取首页 右上角的消息表示  证明登录成功
        :return:
        """
        return self.get_by_element.get_element(self.section, 'message')

    def get_account_element(self):
        """
        首页左上角的账号按钮
        :return:
        """
        return self.get_by_element.get_element(self.section, 'account')

    def get_loginout_button_element(self):
        """
        设置里面的退出登录按钮
        :return:
        """
        return self.get_by_element.get_element(self.section, 'logout_button')

    def get_login_logo_element(self):
        """
        登录页面的logo标识
        :return:
        """
        return self.get_by_element.get_element(self.section, 'login_logo')

