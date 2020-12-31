from Common.base_page import BasePage
from Common.config_untils import local_config
from Common.element_date_utils import ElementDateUtils
from Common.log_utils import logger
from Common.browser import Browser
import unittest

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url=local_config.get_url
    def setUp(self) -> None:
        self.base_page=BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.impl_wait()
        self.base_page.open_url(self.url)
    def tearDown(self) -> None:
        self.base_page.quite()
    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('所有用例执行完毕')