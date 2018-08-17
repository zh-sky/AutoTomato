from appium import webdriver
from Util.write_user_command import WriteUserCommand
import time

# iPhone_Simulator = True
iPhone_Simulator = False


class BaseDriver:
    # def __init__(self, i):
    #     self.write_file = WriteUserCommand()
    #     self.port = self.write_file.get_value('user_info_'+str(i), 'port')
    #     self.device_name = self.write_file.get_value('user_info_'+str(i), 'deviceName')

    def iOS_driver(self, i):

        write_file = WriteUserCommand()
        port = write_file.get_value('user_info_' + str(i), 'port')
        device_name = write_file.get_value('user_info_' + str(i), 'deviceName')
        desired_capabilities = {
            'automationName': 'XCUITest',
            'platformName': 'iOS'
            # 'xcodeOrgId': 'HY7HF3W8R5',
            # 'xcodeSigningId': 'iPhone Developer'
        }
        if iPhone_Simulator:
            file_path = '/Users/mike/Desktop/baidu/Tomasky.app'
            desired_capabilities['deviceName'] = 'iPhone Simulator'
            desired_capabilities['platformVersion'] = '11.4'

        else:
            file_path = '/Users/mike/Desktop/Tomasky.app'
            desired_capabilities['udid'] = device_name
            desired_capabilities['deviceName'] = 'iPhone 6s'
            desired_capabilities['platformVersion'] = '11.4.1'

        desired_capabilities['app'] = file_path
        print("http://127.0.0.1:"+port+"/wd/hub")
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", desired_capabilities)
        time.sleep(10)
        if driver.is_app_installed('com.yodfz.FanQie') is not True:
            driver.switch_to.alert.accept()
        return driver

    def Android_driver(self):
        pass
        # xcodebuild - project
        # WebDriverAgent.xcodeproj - scheme
        # WebDriverAgentRunner - destination
        # 'id=d69d11788a251a64fc31dfbc93c9053cfca5cbca'
        # test


if __name__ == '__main__':
    base_driver = BaseDriver()
    ios_driver = base_driver.iOS_driver(0)
