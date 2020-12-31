from Element_infos.login_pages import LoginPages
from Element_infos.main_page.main_pages import MainPage
from Common.config_untils import local_config
from Common.browser import Browser

class LoginAction():
    def __init__(self,driver):
        self.login_page=LoginPages(driver)

    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_default_success(self,username=local_config.user_name,password=local_config.password):
        self.login_action(username,password)
        mainpage=MainPage(self.login_page.driver)
        value=mainpage.get_text(mainpage.user_name_text)
        return value


if __name__ == '__main__':
    driver=Browser().get_driver()
    driver.get(local_config.get_url)
    element=LoginAction(driver)
    a=element.login_default_success()
    print(a)

