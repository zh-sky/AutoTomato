from Case.tomato_case import ParameTestCase


class LoginCase(ParameTestCase):

    def test_login_success(self):
        """
        测试登录成功
        :return:
        """
        flag = self.login_business.login_pass()
        self.assertTrue(flag, '登录失败')
        # self.login_business.login_out()

    def test_login_error(self):
        """
        测试登录失败
        :return: Boolean
        """
        flag_user = self.login_business.login_user_error()
        self.assertTrue(flag_user, '未捕获到"您输入的账号未注册"')
        flag_password = self.login_business.login_password_error()
        self.assertTrue(flag_password, '未捕获到"您输入的密码错误"')
