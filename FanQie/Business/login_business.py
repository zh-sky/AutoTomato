from Handle.login_handle import LoginHandle


class LoginBusiness:
    """
    获取登录页面所有业务
    """
    def __init__(self, i):
        self.login_handle = LoginHandle(i)

    def login_pass(self):
        """
        登录成功
        """
        self.login_handle.send_username('13666666666')
        self.login_handle.send_password('111111')
        self.login_handle.click_login()

    def login_user_error(self):
        """
        用户名错误
        """
        self.login_handle.send_username('13666666667')
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
