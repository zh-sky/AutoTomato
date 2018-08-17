from Handle.login_handle import LoginHandle
import time


class LoginBusiness:
    """
    获取登录页面所有业务
    """
    def __init__(self, driver):
        self.login_handle = LoginHandle(driver, 'login_element')

    def login_pass(self):
        """
        登录成功
        """
        self.login_handle.send_username('13666666666')
        self.login_handle.send_password('111111')
        self.login_handle.click_login()
        time.sleep(1)
        if self.login_handle.is_login_success():
            return True
        return False

    def login_out(self):
        """
        退出登录
        :return: Boolean
        """
        self.login_handle.click_account_button()
        self.login_handle.click_login_out()
        time.sleep(1)
        self.login_handle.login_page.driver.switch_to_alert().accept()
        # if self.login_handle.is_login_out_success():
        #     return True
        # return False

    def login_user_error(self):
        """
        用户名错误
        """
        self.login_handle.send_username('13666666678')
        self.login_handle.send_password('111111')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_toast('您输入的账号未注册')
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        """
        密码错误
        """
        self.login_handle.send_username('13666666666')
        self.login_handle.send_password('111117')
        self.login_handle.click_login()
        password_flag = self.login_handle.get_fail_toast('您输入的密码不正确')
        if password_flag:
            return True
        else:
            return False

