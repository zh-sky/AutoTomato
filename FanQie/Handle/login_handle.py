from Page.login_page import LoginPage


class LoginHandle:
    """
    所有登录页面的操作
    """
    def __init__(self, driver, section):
        self.login_page = LoginPage(driver, section)

    def send_username(self, username):
        """
        输入用户名
        """
        self.login_page.get_username_element().clear()
        self.login_page.get_username_element().send_keys(username)

    def send_password(self, password):
        """
        输入密码
        """
        self.login_page.get_password_element().clear()
        self.login_page.get_password_element().send_keys(password)

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

    def is_login_success(self):
        """
        根据页面是否出现相应的元素  例:title 来判断是否登录成功
        :return: Boolean
        """
        if self.login_page.get_content_page_status_element() is not None:
            return True
        else:
            return False

    def click_account_button(self):
        """
        点击首页的账号按钮  进入设置页面
        :return:
        """
        self.login_page.get_account_element()[0].click()

    def click_login_out(self):
        """
        点击退出登录按钮
        :return:
        """
        self.login_page.get_loginout_button_element().click()

    def is_login_out_success(self):
        """
        退出登录是否成功  根据登录页面的logo标识判断
        :return:
        """
        if self.login_page.get_login_logo_element() is not None:
            return True
        return False
