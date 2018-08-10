from Page.login_page import LoginPage


class LoginHandle:
    """
    所有登录页面的操作
    """
    def __init__(self, i):
        self.login_page = LoginPage(i)

    def send_username(self, username):
        """
        输入用户名
        """
        self.login_page.get_username_element().send_keys(username)

    def send_password(self, password):
        """
        输入密码
        """
        self.login_page.get_username_element().send_keys(password)

    def click_login(self):
        """
        点击登录按钮
        """
        self.login_page.get_login_button_element().click()

    def get_fail_toast(self, message):
        """
        获取toast 根据返回信息判断是否获取到相应数据
        @:param message: 预期得到的toast信息
        """
        toast_element = self.login_page.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False
