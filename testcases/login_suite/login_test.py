import unittest
from actions.login_action import LoginAction
from Common.browser import Browser
from Common.base_page import BasePage
from Common.config_untils import local_config
from Common.log_utils import logger
from actions.select_entrance import Select_Entrance
from Common.selenium_base_case import SeleniumBaseCase

class LoginTest(SeleniumBaseCase):


    def test_login_success(self):
        login_action=LoginAction(self.base_page.driver)
        text1=login_action.login_default_success()
        self.assertEqual(text1,local_config.user_name_text,'登录失败，请检查对应用户姓名是否填写正确')
        logger.info('用户登录校验成功')
        select_action=Select_Entrance(self.base_page.driver)
        select_action.select_entrance()
        self.base_page.wait(3)
if __name__ == '__main__':
    unittest.main()

