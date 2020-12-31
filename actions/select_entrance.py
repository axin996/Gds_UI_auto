from Element_infos.main_page.main_pages import MainPage
from Common.log_utils import logger
class Select_Entrance():
    def __init__(self,driver):
        self.main_page=MainPage(driver)

    def select_entrance(self):
        self.main_page.click_system_link()
        logger.info('点击进入系统入口')
        self.main_page.wait(2)
        self.main_page.click_system_name()
        logger.info('点击变更管理')
        self.main_page.wait(2)
        self.main_page.click_system_event()
