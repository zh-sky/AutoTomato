from appium import webdriver
import time

desired_capabilities = {
            'automationName': 'XCUITest',
            'platformName': 'iOS',
            'deviceName': 'iPhone Simulator',
            'platformVersion': '11.4',
            'app': '/Users/mike/Desktop/baidu/Tomasky.app'
        }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)
time.sleep(2)
driver.find_element_by_accessibility_id('id_txfAccount').clear()
driver.find_element_by_accessibility_id('id_txfAccount').send_keys(13666666666)
driver.find_element_by_accessibility_id('id_txfPwd').clear()
driver.find_element_by_accessibility_id('id_txfPwd').send_keys(111111)
# print(driver.find_element_by_accessibility_id('id_txfPwd'))
driver.find_element_by_accessibility_id('id_btnLogin').click()
time.sleep(1)
driver.find_element_by_accessibility_id('id_main_room').click()
time.sleep(1)
elements = driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeButton'")
# print(len(elements))
# print(elements)
# print(elements[107])
elements[65].click()
driver.find_element_by_accessibility_id('id_red_button').click()
